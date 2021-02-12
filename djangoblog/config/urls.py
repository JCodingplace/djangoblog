from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog import views as blog_views


urlpatterns = [
    path(
        'admin/', admin.site.urls
    ),
    path(
        'api/blog/preview',
        blog_views.BlogPreviewAPI.as_view(),
        name="BlogBlogPreviewAPI"
    ),
    path(
        'api/blog/detail/<slug:title_slug>',
        blog_views.BlogDetailAPI.as_view(),
        name="BlogBlogDetailAPI"
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
