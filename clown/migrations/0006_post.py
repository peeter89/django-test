# Generated by Django 2.0.4 on 2018-04-26 10:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clown', '0005_auto_20180426_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.CharField(max_length=250)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_publish', models.DateTimeField(default=datetime.date(2018, 4, 26))),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clown.Author')),
                ('hashtag', models.ManyToManyField(help_text='Select a Hashtag for Post', to='clown.Hashtag')),
            ],
            options={
                'ordering': ['date_create'],
            },
        ),
    ]
