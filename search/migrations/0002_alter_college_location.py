# Generated by Django 4.2.4 on 2023-09-01 13:19

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(max_length=100, srid=4326),
        ),
    ]
