# Generated by Django 4.2.1 on 2023-12-15 12:22

from django.db import migrations, models
import prayerconnect.prayerconnectuploadfiles


class Migration(migrations.Migration):

    dependencies = [
        ('prayerconnect', '0002_alter_prayerconnect_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='prayerconnect',
            name='gallery_image_path_1',
            field=models.ImageField(blank=True, null=True, upload_to=prayerconnect.prayerconnectuploadfiles.prayer_connect_upload_image_path, verbose_name='Gallery image 1'),
        ),
        migrations.AddField(
            model_name='prayerconnect',
            name='gallery_image_path_2',
            field=models.ImageField(blank=True, null=True, upload_to=prayerconnect.prayerconnectuploadfiles.prayer_connect_upload_image_path, verbose_name='Gallery image 2'),
        ),
        migrations.AddField(
            model_name='prayerconnect',
            name='gallery_image_path_3',
            field=models.ImageField(blank=True, null=True, upload_to=prayerconnect.prayerconnectuploadfiles.prayer_connect_upload_image_path, verbose_name='Gallery image 3'),
        ),
        migrations.AddField(
            model_name='prayerconnect',
            name='gallery_image_path_4',
            field=models.ImageField(blank=True, null=True, upload_to=prayerconnect.prayerconnectuploadfiles.prayer_connect_upload_image_path, verbose_name='Gallery image 4'),
        ),
    ]
