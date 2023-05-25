# Generated by Django 4.2.1 on 2023-05-23 18:51

import homeactivities.uploadfiles
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activitie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Intro tile')),
                ('alias_title', models.CharField(max_length=255, verbose_name='Sub tile')),
                ('icon_image_path', models.ImageField(blank=True, null=True, upload_to=homeactivities.uploadfiles.upload_image_path, verbose_name='Icon image')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'ordering': ('title', 'alias_title'),
            },
        ),
        migrations.CreateModel(
            name='HomeActivitie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Intro tile')),
                ('sub_title', models.CharField(max_length=255, verbose_name='Sub tile')),
                ('text', models.CharField(max_length=1024, verbose_name='Intro text')),
                ('background_image_path', models.ImageField(blank=True, null=True, upload_to=homeactivities.uploadfiles.upload_image_path, verbose_name='Background image')),
                ('icon_image_path', models.ImageField(blank=True, null=True, upload_to=homeactivities.uploadfiles.upload_image_path, verbose_name='Icon image')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('activities', models.ManyToManyField(to='homeactivities.activitie')),
            ],
            options={
                'db_table': 'homeactivities',
                'ordering': ('title', 'sub_title', 'created_at'),
            },
        ),
    ]