# Generated by Django 2.2.5 on 2019-09-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('artist_name', models.CharField(max_length=50)),
                ('subject', models.TextField()),
                ('origin', models.CharField(max_length=50)),
                ('medium', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='image/')),
            ],
            options={
                'permissions': [('special_access', 'Can read all paintings')],
            },
        ),
    ]