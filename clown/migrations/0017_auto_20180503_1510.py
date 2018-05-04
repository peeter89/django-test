# Generated by Django 2.0.4 on 2018-05-03 13:10

import clown.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clown', '0016_auto_20180503_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(default=2, height_field='height_field', upload_to=clown.models.upload_location_photo, width_field='width_field'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
