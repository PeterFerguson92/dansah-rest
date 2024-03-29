# Generated by Django 4.2.1 on 2023-07-28 20:10

from django.db import migrations, models
import prayercity.prayercityuploadfiles
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrayerCity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('alias', models.CharField(default='prayer-city', editable=False, max_length=255, verbose_name='Alias')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('short_description', models.CharField(max_length=255, verbose_name='Short Description')),
                ('full_description', models.TextField(blank=True, max_length=1024, verbose_name='Full Description')),
                ('cover_image_path', models.ImageField(blank=True, null=True, upload_to=prayercity.prayercityuploadfiles.prayer_city_upload_image_path, verbose_name='Cover image')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Prayer City',
                'ordering': ('title', 'created_at'),
            },
        ),
    ]
