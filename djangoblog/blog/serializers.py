from rest_framework import serializers
from .models import Blogpost


class BlogPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['title', 'title_slug', 'subtitle', 'thumbnail',
                  'published_date', ]


class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['title', 'title_slug', 'subtitle', 'thumbnail',
                  'published_date', 'body', ]
