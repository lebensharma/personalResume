# Generated by Django 3.1.7 on 2021-03-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newedit',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=200)),
                ('content', models.TextField(max_length=3000)),
                ('thumbnailimage', models.ImageField(default='', upload_to='editsimg/')),
                ('author', models.TextField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False, verbose_name='')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('content', models.TextField(max_length=3000)),
                ('thimg', models.ImageField(default='', upload_to='img/')),
                ('author', models.TextField(default='')),
                ('time_stamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
