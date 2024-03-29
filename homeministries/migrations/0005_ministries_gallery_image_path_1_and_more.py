# Generated by Django 4.2.1 on 2023-12-15 12:22

from django.db import migrations, models
import homeministries.homeministriesuploadfiles


class Migration(migrations.Migration):

    dependencies = [
        ('homeministries', '0004_alter_homeministries_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministries',
            name='gallery_image_path_1',
            field=models.ImageField(blank=True, null=True, upload_to=homeministries.homeministriesuploadfiles.home_ministries_upload_image_path, verbose_name='Gallery image 1'),
        ),
        migrations.AddField(
            model_name='ministries',
            name='gallery_image_path_2',
            field=models.ImageField(blank=True, null=True, upload_to=homeministries.homeministriesuploadfiles.home_ministries_upload_image_path, verbose_name='Gallery image 2'),
        ),
        migrations.AddField(
            model_name='ministries',
            name='gallery_image_path_3',
            field=models.ImageField(blank=True, null=True, upload_to=homeministries.homeministriesuploadfiles.home_ministries_upload_image_path, verbose_name='Gallery image 3'),
        ),
        migrations.AddField(
            model_name='ministries',
            name='gallery_image_path_4',
            field=models.ImageField(blank=True, null=True, upload_to=homeministries.homeministriesuploadfiles.home_ministries_upload_image_path, verbose_name='Gallery image 4'),
        ),
    ]
