# Generated by Django 4.2 on 2023-04-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_homepageleftcontent2_remove_homepageleftcontent_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageContent2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=40, verbose_name='Home Page Content2 Title 1')),
                ('title2', models.CharField(max_length=40, verbose_name='Home Page Content2 Title 2')),
                ('text', models.TextField(verbose_name='Home Page Content2 Text')),
                ('btn_name', models.CharField(max_length=25, verbose_name='Home Page Content2 Button Name')),
                ('img', models.ImageField(upload_to='images', verbose_name='Home Page Content2 Image')),
            ],
            options={
                'verbose_name': 'HomePageContent2',
                'verbose_name_plural': 'HomePageContent2',
            },
        ),
        migrations.DeleteModel(
            name='HomePageLeftContent2',
        ),
    ]