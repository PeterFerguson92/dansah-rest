# Generated by Django 4.2.1 on 2023-08-22 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeministries', '0002_alter_homeministries_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeministries',
            options={'ordering': ('title', 'created_at'), 'verbose_name': 'Ministry', 'verbose_name_plural': 'Ministries'},
        ),
        migrations.AlterModelOptions(
            name='ministries',
            options={'ordering': ('name', 'created_at'), 'verbose_name': 'Home Ministry', 'verbose_name_plural': 'Home Ministries'},
        ),
    ]