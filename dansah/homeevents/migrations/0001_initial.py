# Generated by Django 4.2.1 on 2023-05-23 18:51

import homeevents.uploadfiles
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Ministries material title')),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('icon_image_path', models.ImageField(blank=True, null=True, upload_to=homeevents.uploadfiles.upload_image_path, verbose_name='Icon image')),
                ('date_detail_1', models.CharField(max_length=255, verbose_name='Date details')),
                ('date_detail_2', models.CharField(max_length=255, verbose_name='Date details 2')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'ordering': ('title', 'description', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='HomeEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Intro tile')),
                ('sub_title', models.CharField(max_length=255, verbose_name='Sub tile')),
                ('icon_image_path', models.ImageField(blank=True, null=True, upload_to=homeevents.uploadfiles.upload_image_path, verbose_name='Icon image')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('events', models.ManyToManyField(to='homeevents.event')),
            ],
            options={
                'ordering': ('title', 'sub_title', 'created_at'),
            },
        ),
    ]