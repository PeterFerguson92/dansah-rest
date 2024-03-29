# Generated by Django 4.2.1 on 2023-07-28 20:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import leadershipinstitute.leadershipInstitueuploadfiles
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, default='', max_length=1024, verbose_name='Description')),
                ('document', models.FileField(blank=True, null=True, upload_to='leadershipinstitute/materials/assesments', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx'])], verbose_name='Upload Assesment Document')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Assesments',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, default='', max_length=1024, verbose_name='Description')),
                ('document', models.FileField(blank=True, null=True, upload_to='leadershipinstitute/materials/assignments', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx'])], verbose_name='Upload Assignment Document')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Assignments',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('cover_image_path', models.ImageField(blank=True, null=True, upload_to=leadershipinstitute.leadershipInstitueuploadfiles.leadership_institute_categories_upload_image_path, verbose_name='Cover image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('name', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(default='', max_length=1024, verbose_name='Description')),
                ('document', models.FileField(blank=True, null=True, upload_to='leadershipinstitute/materials/readings', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Upload Pdf')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Reading Materials',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(default='', max_length=1024, verbose_name='Description')),
                ('link', models.CharField(max_length=255, verbose_name='Link')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name_plural': 'Video Materials',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('assesments', models.ManyToManyField(to='leadershipinstitute.assesment')),
                ('assignments', models.ManyToManyField(to='leadershipinstitute.assignment')),
                ('readings', models.ManyToManyField(to='leadershipinstitute.reading')),
                ('videos', models.ManyToManyField(to='leadershipinstitute.video')),
            ],
            options={
                'verbose_name_plural': 'Materials',
                'ordering': ('name', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='LeadershipInstitute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('alias', models.CharField(default='leadership-institute', editable=False, max_length=255, verbose_name='Alias')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('short_description', models.CharField(max_length=255, verbose_name='Short Description')),
                ('full_description', models.TextField(blank=True, max_length=1024, verbose_name='Full Description')),
                ('cover_image_path', models.ImageField(blank=True, null=True, upload_to=leadershipinstitute.leadershipInstitueuploadfiles.leadership_institute_upload_image_path, verbose_name='Cover image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('categories', models.ManyToManyField(to='leadershipinstitute.category')),
            ],
            options={
                'verbose_name_plural': 'Leadership Institute',
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('short_description', models.CharField(default='', max_length=255, verbose_name='Short Description')),
                ('full_description', models.TextField(default='', max_length=1024, verbose_name='Full Description')),
                ('cover_image_path', models.ImageField(blank=True, null=True, upload_to=leadershipinstitute.leadershipInstitueuploadfiles.leadership_institute_course_upload_image_path, verbose_name='Cover image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leadershipinstitute.category')),
                ('materials', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leadershipinstitute.material')),
            ],
            options={
                'verbose_name_plural': 'Courses',
                'ordering': ('name', 'created_at'),
            },
        ),
    ]
