# Generated by Django 2.0.4 on 2018-04-26 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clown', '0004_auto_20180426_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='hashtag',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
