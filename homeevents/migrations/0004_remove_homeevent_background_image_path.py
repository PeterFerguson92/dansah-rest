# Generated by Django 4.2.1 on 2023-07-30 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeevents', '0003_remove_event_background_image_path_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeevent',
            name='background_image_path',
        ),
    ]