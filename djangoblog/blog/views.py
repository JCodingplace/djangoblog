from rest_framework.generics import ListAPIView, RetrieveAPIView
from common.generics import CachedGenericView
from .models import Blogpost
from .serializers import BlogPreviewSerializer, BlogDetailSerializer
from .paginations import BlogPreviewPagination


class BlogPreviewAPI(CachedGenericView, ListAPIView):
    queryset = Blogpost.objects\
        .filter(is_published=True)\
        .order_by("-published_date")
    serializer_class = BlogPreviewSerializer
    pagination_class = BlogPreviewPagination
    timeout = 60 * 24


class BlogDetailAPI(CachedGenericView, RetrieveAPIView):
    queryset = Blogpost.objects
    serializer_class = BlogDetailSerializer
    lookup_field = 'title_slug'
    timeout = 60 * 24
