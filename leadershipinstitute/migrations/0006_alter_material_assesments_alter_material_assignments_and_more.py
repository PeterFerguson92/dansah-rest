# Generated by Django 4.2.1 on 2023-07-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leadershipinstitute', '0005_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='assesments',
            field=models.ManyToManyField(blank=True, to='leadershipinstitute.assesment'),
        ),
        migrations.AlterField(
            model_name='material',
            name='assignments',
            field=models.ManyToManyField(blank=True, to='leadershipinstitute.assignment'),
        ),
        migrations.AlterField(
            model_name='material',
            name='readings',
            field=models.ManyToManyField(blank=True, to='leadershipinstitute.reading'),
        ),
        migrations.AlterField(
            model_name='material',
            name='videos',
            field=models.ManyToManyField(blank=True, to='leadershipinstitute.video'),
        ),
    ]
