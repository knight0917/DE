# Generated by Django 4.0.3 on 2022-03-31 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_userdetail_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='slug',
            field=models.SlugField(default='', null='False'),
            preserve_default='False',
        ),
    ]
