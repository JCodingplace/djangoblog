# Generated by Django 3.1.6 on 2021-02-11 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('title_slug', models.SlugField(editable=False, unique=True, verbose_name='Title Slug')),
                ('subtitle', models.CharField(blank=True, max_length=144, verbose_name='Subtitle')),
                ('thumbnail', models.ImageField(upload_to='blogs', verbose_name='Thumbnail')),
                ('body', models.JSONField(verbose_name='Body')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('last_change_date', models.DateTimeField(auto_now=True, verbose_name='Last Change Date')),
                ('published_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='First time published')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is Published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blogs', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Blogpost',
                'verbose_name_plural': 'Blogposts',
                'ordering': ('is_published', '-published_date', '-last_change_date'),
            },
        ),
    ]
