# Generated by Django 4.0.3 on 2022-04-05 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_userdetail_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='photo',
            new_name='image',
        ),
    ]
