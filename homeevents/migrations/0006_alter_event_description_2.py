# Generated by Django 4.2.1 on 2023-08-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeevents', '0005_alter_event_description_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description_2',
            field=models.TextField(blank=True, max_length=1024, verbose_name='Description '),
        ),
    ]