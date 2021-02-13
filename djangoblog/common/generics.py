from rest_framework.generics import GenericAPIView
from django.core.cache import cache


class CachedGenericView(GenericAPIView):
    timeout = 60 * 15
    cache_prefix = None

    def get_cache_prefix(self):
        if self.cache_prefix is not None:
            return self.cache_prefix
        view = self.__class__.__name__
        model = self.queryset.model.__name__
        cache_prefix = f"{view}_{model}"
        return cache_prefix

    def get_cached_queryset(self):
        cache_prefix = self.get_cache_prefix()
        cached_queryset = cache.get(cache_prefix)
        return cached_queryset

    def set_cached_queryset(self, queryset):
        cache_prefix = self.get_cache_prefix()
        cache.set(cache_prefix, queryset, timeout=self.timeout)

    def get_queryset(self):
        cached_queryset = self.get_cached_queryset()
        if cached_queryset is not None:
            return cached_queryset
        queryset = super().get_queryset()
        self.set_cached_queryset(queryset)
        return queryset

    def get_cached_object(self):
        cache_prefix = self.get_cache_prefix()
        key = f"{cache_prefix}_{self.lookup_field}"
        cached_object = cache.get(key)
        return cached_object

    def set_cached_object(self, instance):
        cache_prefix = self.get_cache_prefix()
        key = f"{cache_prefix}_{self.lookup_field}"
        cache.set(key, instance, timeout=self.timeout)

    def get_object(self):
        cached_object = self.get_cached_object()
        if cached_object is not None:
            return cached_object
        instance = super().get_object()
        self.set_cached_object(instance)
        return instance
