# Generated by Django 3.0.8 on 2020-10-24 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='identifier',
        ),
    ]