# Generated by Django 4.2 on 2023-04-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_homecontactpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExploreContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Explore Content Title')),
                ('title_hy', models.CharField(max_length=80, null=True, verbose_name='Explore Content Title')),
                ('title_ru', models.CharField(max_length=80, null=True, verbose_name='Explore Content Title')),
                ('title_en', models.CharField(max_length=80, null=True, verbose_name='Explore Content Title')),
                ('img', models.ImageField(upload_to='images', verbose_name='Explore Content Image')),
            ],
        ),
        migrations.CreateModel(
            name='ExploreContentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Explore Content List Title')),
                ('title_hy', models.CharField(max_length=30, null=True, verbose_name='Explore Content List Title')),
                ('title_ru', models.CharField(max_length=30, null=True, verbose_name='Explore Content List Title')),
                ('title_en', models.CharField(max_length=30, null=True, verbose_name='Explore Content List Title')),
                ('subtitle', models.CharField(max_length=30, verbose_name='Explore Content List SubTitle')),
                ('subtitle_hy', models.CharField(max_length=30, null=True, verbose_name='Explore Content List SubTitle')),
                ('subtitle_ru', models.CharField(max_length=30, null=True, verbose_name='Explore Content List SubTitle')),
                ('subtitle_en', models.CharField(max_length=30, null=True, verbose_name='Explore Content List SubTitle')),
            ],
        ),
        migrations.CreateModel(
            name='ExploreTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=20, verbose_name='Explore Title 1')),
                ('title1_hy', models.CharField(max_length=20, null=True, verbose_name='Explore Title 1')),
                ('title1_ru', models.CharField(max_length=20, null=True, verbose_name='Explore Title 1')),
                ('title1_en', models.CharField(max_length=20, null=True, verbose_name='Explore Title 1')),
                ('title2', models.CharField(max_length=20, verbose_name='Explore Title 2')),
                ('title2_hy', models.CharField(max_length=20, null=True, verbose_name='Explore Title 2')),
                ('title2_ru', models.CharField(max_length=20, null=True, verbose_name='Explore Title 2')),
                ('title2_en', models.CharField(max_length=20, null=True, verbose_name='Explore Title 2')),
                ('text', models.TextField(verbose_name='Explore Text')),
                ('text_hy', models.TextField(null=True, verbose_name='Explore Text')),
                ('text_ru', models.TextField(null=True, verbose_name='Explore Text')),
                ('text_en', models.TextField(null=True, verbose_name='Explore Text')),
            ],
            options={
                'verbose_name': 'ExploreTitle',
                'verbose_name_plural': 'ExploreTitle',
            },
        ),
    ]