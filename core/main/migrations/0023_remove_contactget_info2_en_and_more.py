# Generated by Django 4.2 on 2023-04-05 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_contacttitle_text_en_contacttitle_text_hy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactget',
            name='info2_en',
        ),
        migrations.RemoveField(
            model_name='contactget',
            name='info2_hy',
        ),
        migrations.RemoveField(
            model_name='contactget',
            name='info2_ru',
        ),
        migrations.RemoveField(
            model_name='contactget',
            name='info3_en',
        ),
        migrations.RemoveField(
            model_name='contactget',
            name='info3_hy',
        ),
        migrations.RemoveField(
            model_name='contactget',
            name='info3_ru',
        ),
    ]
