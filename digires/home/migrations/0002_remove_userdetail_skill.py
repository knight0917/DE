# Generated by Django 4.0.3 on 2022-03-22 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='skill',
        ),
    ]
