# Generated by Django 4.0.3 on 2022-03-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('skill', models.CharField(max_length=500, null=True)),
                ('web', models.CharField(max_length=800, null=True)),
                ('linkedin', models.CharField(max_length=800, null=True)),
                ('github', models.CharField(max_length=800, null=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('acadqual', models.CharField(max_length=500, null=True)),
                ('workexp', models.CharField(max_length=500, null=True)),
                ('inter', models.CharField(max_length=500, null=True)),
                ('about', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]