# Generated by Django 5.0.3 on 2024-04-01 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links_process', '0004_linksprocess_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linksprocess',
            name='user_id',
        ),
    ]
