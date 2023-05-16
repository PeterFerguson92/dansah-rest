# Generated by Django 4.2.1 on 2023-05-16 20:57

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devotional',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('devotion_title', models.CharField(max_length=255, verbose_name='Devotion title')),
                ('devotion_message', models.TextField(max_length=2048, verbose_name='Devotion message')),
                ('devotion_date', models.DateField(default=datetime.date(2023, 5, 16), verbose_name='Devotion date')),
                ('devotion_created_at', models.DateTimeField(auto_now_add=True)),
                ('devotion_updated_at', models.DateTimeField(auto_now_add=True)),
                ('devotion_monthly', models.BooleanField(default=False, verbose_name='Monthly devotion')),
            ],
            options={
                'ordering': ('devotion_title', 'devotion_date'),
            },
        ),
    ]
