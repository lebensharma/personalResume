# Generated by Django 3.1.7 on 2021-03-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='uname',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
