# Generated by Django 2.0.4 on 2018-05-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clown', '0007_auto_20180426_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.CharField(default='test', max_length=500),
        ),
    ]
