# Generated by Django 4.2.1 on 2023-08-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeevents', '0004_remove_homeevent_background_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description_2',
            field=models.TextField(blank=True, max_length=1024, verbose_name='Description 2'),
        ),
    ]
