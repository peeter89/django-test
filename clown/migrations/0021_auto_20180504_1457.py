# Generated by Django 2.0.4 on 2018-05-04 12:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clown', '0020_auto_20180503_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2018, 5, 4, 12, 57, 35, 427472, tzinfo=utc)),
            preserve_default=False,
        ),
    ]