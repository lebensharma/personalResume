# Generated by Django 3.1.7 on 2021-03-13 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time_stamp',
        ),
    ]
