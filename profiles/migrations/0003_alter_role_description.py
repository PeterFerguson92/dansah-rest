# Generated by Django 4.2.1 on 2023-08-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_cover_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='description',
            field=models.TextField(max_length=1024, verbose_name='Description'),
        ),
    ]
