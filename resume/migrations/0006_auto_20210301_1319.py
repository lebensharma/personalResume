# Generated by Django 3.1.7 on 2021-03-01 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20210301_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='connect',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='connect',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
