# Generated by Django 5.0.3 on 2024-03-29 19:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_rename_links_link'),
        ('playlists', '0002_alter_playlists_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Playlists',
            new_name='Playlist',
        ),
    ]
