# Generated by Django 4.2.1 on 2023-08-22 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeministries', '0003_alter_homeministries_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeministries',
            options={'ordering': ('title', 'created_at'), 'verbose_name': 'Home Ministry', 'verbose_name_plural': 'Home Ministry'},
        ),
        migrations.AlterModelOptions(
            name='ministries',
            options={'ordering': ('name', 'created_at'), 'verbose_name': 'Ministry', 'verbose_name_plural': 'Ministries'},
        ),
    ]