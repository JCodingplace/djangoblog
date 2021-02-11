from django.contrib import admin
from .models import Blogpost


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ("title", "creation_date", "last_change_date",
                    "published_date", "is_published", )
    readonly_fields = ("creation_date", "last_change_date", "published_date",
                       "title_slug")
    search_fields = ("title_slug", )
