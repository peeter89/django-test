# Generated by Django 2.0.4 on 2018-04-24 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_create', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Hashtag name', max_length=50, unique=True)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clown.Author')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.CharField(max_length=250)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('Hashtag', models.ManyToManyField(help_text='Select a Hashtag for Post', to='clown.Hashtag')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clown.Author')),
            ],
            options={
                'ordering': ['date_create'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter state name (e.g. publish, unpublish...)', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clown.State'),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='state',
            field=models.ForeignKey(help_text='Tag state', on_delete=django.db.models.deletion.PROTECT, to='clown.State'),
        ),
    ]
