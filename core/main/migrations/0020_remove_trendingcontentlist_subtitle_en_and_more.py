# Generated by Django 4.2 on 2023-04-05 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_trendingcontentlist_trendinglastcontent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trendingcontentlist',
            name='subtitle_en',
        ),
        migrations.RemoveField(
            model_name='trendingcontentlist',
            name='subtitle_hy',
        ),
        migrations.RemoveField(
            model_name='trendingcontentlist',
            name='subtitle_ru',
        ),
        migrations.RemoveField(
            model_name='trendingcontentlist',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='trendingcontentlist',
            name='title_hy',
        ),
        migrations.RemoveField(
            model_name='trendingcontentlist',
            name='title_ru',
        ),
    ]
