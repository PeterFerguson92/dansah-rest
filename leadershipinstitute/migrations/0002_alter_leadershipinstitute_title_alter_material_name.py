# Generated by Django 4.2.1 on 2023-07-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadershipinstitute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadershipinstitute',
            name='title',
            field=models.CharField(default='Leadership Institute', max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(default='Course Material', max_length=255, verbose_name='Name'),
        ),
    ]
