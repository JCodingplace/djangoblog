import os
import json
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings
from distutils.dir_util import copy_tree


def blog_image_directory_path(instance, filename):
    blogpath = instance.title_slug.replace('-', '_')
    suffix = filename.split('.')[1]
    image_filename = f"{blogpath}_thumbnail"
    fullpath = f"blogs/{blogpath}/{image_filename}.{suffix}"
    return fullpath


class Blogpost(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="blogs",
        verbose_name=_("Author"),
        on_delete=models.PROTECT
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=40
    )
    title_slug = models.SlugField(
        verbose_name=_("Title Slug"),
        unique=True,
        editable=False,
        db_index=True
    )
    subtitle = models.CharField(
        verbose_name=_("Subtitle"),
        max_length=144,
        blank=True
    )
    thumbnail = models.ImageField(
        verbose_name=_("Thumbnail"),
        upload_to=blog_image_directory_path
    )
    body = models.JSONField(
        verbose_name=_("Body")
    )
    creation_date = models.DateTimeField(
        verbose_name=_("Creation Date"),
        auto_now_add=True
    )
    last_change_date = models.DateTimeField(
        verbose_name=_("Last Change Date"),
        auto_now=True
    )
    published_date = models.DateTimeField(
        verbose_name=_("First time published"),
        blank=True,
        null=True,
        editable=False
    )
    is_published = models.BooleanField(
        verbose_name=_("Is Published"),
        default=False
    )

    class Meta:
        verbose_name = _("Blogpost")
        verbose_name_plural = _("Blogposts")
        ordering = ("-is_published", "-published_date", "-last_change_date", )

    def save(self, *args, **kwargs):
        latest_title_slug = slugify(self.title)
        if self.title_slug and latest_title_slug != self.title_slug:
            self.update_backup_directory_on_title_change()

        self.title_slug = slugify(self.title)
        if self.is_published and not self.published_date:
            self.published_date = timezone.now()

        self.create_file()
        super().save(*args, **kwargs)

    def create_file(self):
        # TODO Fix Security issue -
        # - it's possible to get any files via curl
        name = self.title_slug.replace('-', '_')
        path = os.path.join(settings.MEDIA_ROOT, 'blogs', name)
        if not os.path.exists(path):
            os.makedirs(path)
        existing_version_count = len([
            version
            for version in os.listdir(path)
            if version.endswith(".json")
        ])
        timestamp = timezone.now().strftime("%Y_%m_%d__%H_%M_%S")
        filename = f"{name}__{timestamp}__v{existing_version_count + 1}.json"
        f = open(os.path.join(path, filename), "w")
        f.write(json.dumps(self.body))
        f.close()

    def update_backup_directory_on_title_change(self):
        # TODO Handle Image Path upload
        if not self.title_slug:
            return

        old_name = self.title_slug.replace('-', '_')
        old_path = os.path.join(settings.MEDIA_ROOT, 'blogs', old_name)
        old_path_exists = os.path.exists(old_path)

        new_name = slugify(self.title).replace('-', '_')
        new_path = os.path.join(settings.MEDIA_ROOT, 'blogs', new_name)
        new_path_exists = os.path.exists(new_path)

        if old_path_exists and not new_path_exists:
            copy_tree(old_path, new_path)
