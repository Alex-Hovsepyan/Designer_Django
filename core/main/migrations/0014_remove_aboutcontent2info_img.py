# Generated by Django 4.2 on 2023-04-04 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_aboutcontent2info_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutcontent2info',
            name='img',
        ),
    ]