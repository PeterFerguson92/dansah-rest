# Generated by Django 4.2.1 on 2023-08-18 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='title',
            field=models.CharField(choices=[('FACEBOOK', 'Facebook'), ('INSTAGRAM', 'Instagram'), ('TWITTER', 'Twitter'), ('YOUTUBE', 'Youtube')], max_length=50),
        ),
    ]