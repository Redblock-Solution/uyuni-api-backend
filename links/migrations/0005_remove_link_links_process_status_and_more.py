# Generated by Django 5.0.3 on 2024-03-30 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_alter_link_youtube_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='links_process_status',
        ),
        migrations.RemoveField(
            model_name='link',
            name='youtube_id',
        ),
    ]