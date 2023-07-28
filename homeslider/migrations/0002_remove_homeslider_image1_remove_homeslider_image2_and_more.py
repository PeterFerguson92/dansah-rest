# Generated by Django 4.2.1 on 2023-07-28 22:22

from django.db import migrations, models
import homeslider.homeslidersuploadfiles


class Migration(migrations.Migration):

    dependencies = [
        ('homeslider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeslider',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='homeslider',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='homeslider',
            name='image3',
        ),
        migrations.AddField(
            model_name='homeslider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=homeslider.homeslidersuploadfiles.home_sliders_upload_image_path, verbose_name='Image'),
        ),
    ]
