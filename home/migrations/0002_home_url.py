# Generated by Django 4.2.1 on 2023-12-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='url',
            field=models.CharField(default='test', max_length=255, verbose_name='Live Event Url'),
            preserve_default=False,
        ),
    ]
