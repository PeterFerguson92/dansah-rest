# Generated by Django 4.2.1 on 2023-08-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='momo_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='MoMo Number'),
        ),
    ]
