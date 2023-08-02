# Generated by Django 4.2.1 on 2023-07-28 20:10

import django.core.validators
from django.db import migrations, models
import powerliving.powerlivinguploadfiles
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPowerLiving',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Monthly Power Living tile')),
                ('description', models.TextField(blank=True, max_length=1024, verbose_name='Description')),
                ('cover_image_path', models.ImageField(blank=True, null=True, upload_to=powerliving.powerlivinguploadfiles.power_living_upload_image_path, verbose_name='Cover image')),
                ('document', models.FileField(blank=True, null=True, upload_to='powerlivingfiles/pdfs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='File upload')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Monthly Power Living',
                'verbose_name_plural': 'Monthly Power Living',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='PowerLiving',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('alias', models.CharField(default='power-living', editable=False, max_length=255, verbose_name='Alias')),
                ('title', models.CharField(max_length=255, verbose_name='Power Living title')),
                ('short_description', models.CharField(max_length=255, verbose_name='Short Description')),
                ('full_description', models.TextField(blank=True, max_length=1024, verbose_name='Full Description')),
                ('cover_image_path', models.ImageField(blank=True, null=True, upload_to=powerliving.powerlivinguploadfiles.power_living_upload_image_path, verbose_name='Cover Image')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('monthly_power_living', models.ManyToManyField(to='powerliving.monthlypowerliving')),
            ],
            options={
                'verbose_name': 'Power Living',
                'verbose_name_plural': 'Power Living',
                'ordering': ('title', 'created_at'),
            },
        ),
    ]