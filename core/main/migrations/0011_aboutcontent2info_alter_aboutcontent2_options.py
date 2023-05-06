# Generated by Django 4.2 on 2023-04-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_aboutcontent_aboutcontent2_abouttitle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent2Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=40, verbose_name='About Content2 Info Title 1')),
                ('title1_hy', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 1')),
                ('title1_ru', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 1')),
                ('title1_en', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 1')),
                ('title2', models.CharField(max_length=40, verbose_name='About Content2 Info Title 2')),
                ('title2_hy', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 2')),
                ('title2_ru', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 2')),
                ('title2_en', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 2')),
                ('title3', models.CharField(max_length=40, verbose_name='About Content2 Info Title 3')),
                ('title3_hy', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 3')),
                ('title3_ru', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 3')),
                ('title3_en', models.CharField(max_length=40, null=True, verbose_name='About Content2 Info Title 3')),
                ('text1', models.TextField(verbose_name='About Content 2 Info Text 1')),
                ('text1_hy', models.TextField(null=True, verbose_name='About Content 2 Info Text 1')),
                ('text1_ru', models.TextField(null=True, verbose_name='About Content 2 Info Text 1')),
                ('text1_en', models.TextField(null=True, verbose_name='About Content 2 Info Text 1')),
                ('text2', models.TextField(verbose_name='About Content 2 Info Text 2')),
                ('text2_hy', models.TextField(null=True, verbose_name='About Content 2 Info Text 2')),
                ('text2_ru', models.TextField(null=True, verbose_name='About Content 2 Info Text 2')),
                ('text2_en', models.TextField(null=True, verbose_name='About Content 2 Info Text 2')),
                ('text3', models.TextField(verbose_name='About Content 2 Info Text 3')),
                ('text3_hy', models.TextField(null=True, verbose_name='About Content 2 Info Text 3')),
                ('text3_ru', models.TextField(null=True, verbose_name='About Content 2 Info Text 3')),
                ('text3_en', models.TextField(null=True, verbose_name='About Content 2 Info Text 3')),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutcontent2',
            options={'verbose_name': 'AboutContents2', 'verbose_name_plural': 'AboutContents2'},
        ),
    ]
