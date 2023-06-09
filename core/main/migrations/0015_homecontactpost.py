# Generated by Django 4.2 on 2023-04-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_aboutcontent2info_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContactPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40, verbose_name='User Name')),
                ('user_surname', models.CharField(max_length=40, verbose_name='User Surname')),
                ('user_email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('user_subject', models.CharField(max_length=50, verbose_name='User Subject')),
                ('user_message', models.TextField(verbose_name='User Message')),
            ],
        ),
    ]
