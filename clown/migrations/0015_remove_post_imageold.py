# Generated by Django 2.0.4 on 2018-05-02 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clown', '0014_auto_20180502_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imageold',
        ),
    ]
