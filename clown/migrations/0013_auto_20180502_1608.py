# Generated by Django 2.0.4 on 2018-05-02 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clown', '0012_auto_20180502_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='imageold',
        ),
    ]