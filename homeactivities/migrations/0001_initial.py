# Generated by Django 4.2.1 on 2023-07-28 20:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prayercity', '0001_initial'),
        ('leadershipinstitute', '0001_initial'),
        ('powerliving', '0001_initial'),
        ('prayerconnect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('leadership_institute', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leadershipinstitute.leadershipinstitute')),
                ('power_living', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerliving.powerliving')),
                ('prayer_city', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prayercity.prayercity')),
                ('prayer_connect', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prayerconnect.prayerconnect')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
                'ordering': ('id',),
            },
        ),
    ]
