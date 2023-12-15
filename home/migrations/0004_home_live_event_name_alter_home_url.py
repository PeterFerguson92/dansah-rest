# Generated by Django 4.2.1 on 2023-12-15 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_home_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='live_event_name',
            field=models.CharField(default='default', max_length=255, verbose_name='Live Event Name'),
        ),
        migrations.AlterField(
            model_name='home',
            name='url',
            field=models.CharField(default='default', max_length=255, verbose_name='Video Id'),
        ),
    ]