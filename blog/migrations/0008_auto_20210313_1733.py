# Generated by Django 3.1.7 on 2021-03-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210313_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.TextField(max_length=15),
        ),
    ]
