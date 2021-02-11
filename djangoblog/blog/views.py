from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Blogpost
from .serializers import BlogPreviewSerializer, BlogDetailSerializer
from .paginations import BlogPreviewPagination


class BlogPreviewAPI(ListAPIView):
    queryset = Blogpost.objects\
        .filter(is_published=True)\
        .order_by("-published_date")
    serializer_class = BlogPreviewSerializer
    pagination_class = BlogPreviewPagination


class BlogDetailAPI(RetrieveAPIView):
    queryset = Blogpost.objects
    serializer_class = BlogDetailSerializer
    lookup_field = 'title_slug'
