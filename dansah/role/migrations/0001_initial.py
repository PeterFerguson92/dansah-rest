# Generated by Django 4.2.1 on 2023-05-22 21:42

import role.uploadfiles
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255, verbose_name='Role type')),
                ('description', models.CharField(max_length=255, verbose_name='Role description')),
                ('icon_image_path', models.ImageField(blank=True, null=True, upload_to=role.uploadfiles.upload_image_path, verbose_name='Icon')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'ordering': ('type', 'description', 'created_at'),
            },
        ),
    ]