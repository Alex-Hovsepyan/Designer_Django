# Generated by Django 4.2 on 2023-04-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_footer_alter_homecontactget_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=30, verbose_name='About Content Title')),
                ('title1_hy', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
                ('title1_ru', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
                ('title1_en', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
                ('title2', models.CharField(max_length=30, verbose_name='About Content Title')),
                ('title2_hy', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
                ('title2_ru', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
                ('title2_en', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
                ('title3', models.CharField(max_length=30, verbose_name='About Content Title')),
                ('title3_hy', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
                ('title3_ru', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
                ('title3_en', models.CharField(max_length=30, null=True, verbose_name='About Content Title')),
            ],
        ),
        migrations.CreateModel(
            name='AboutContent2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=30, verbose_name='About Content 2 Title 1')),
                ('title1_hy', models.CharField(max_length=30, null=True, verbose_name='About Content 2 Title 1')),
                ('title1_ru', models.CharField(max_length=30, null=True, verbose_name='About Content 2 Title 1')),
                ('title1_en', models.CharField(max_length=30, null=True, verbose_name='About Content 2 Title 1')),
                ('title2', models.CharField(max_length=30, verbose_name='About Content 2 Title 2')),
                ('title2_hy', models.CharField(max_length=30, null=True, verbose_name='About Content 2 Title 2')),
                ('title2_ru', models.CharField(max_length=30, null=True, verbose_name='About Content 2 Title 2')),
                ('title2_en', models.CharField(max_length=30, null=True, verbose_name='About Content 2 Title 2')),
                ('img', models.ImageField(upload_to='images', verbose_name='About Content Image')),
                ('text1', models.TextField(verbose_name='About Text 1')),
                ('text1_hy', models.TextField(null=True, verbose_name='About Text 1')),
                ('text1_ru', models.TextField(null=True, verbose_name='About Text 1')),
                ('text1_en', models.TextField(null=True, verbose_name='About Text 1')),
                ('text2', models.TextField(verbose_name='About Text 2')),
                ('text2_hy', models.TextField(null=True, verbose_name='About Text 2')),
                ('text2_ru', models.TextField(null=True, verbose_name='About Text 2')),
                ('text2_en', models.TextField(null=True, verbose_name='About Text 2')),
                ('subtitle', models.CharField(max_length=30, verbose_name='About Content 2 SubTitle')),
                ('subtitle_hy', models.CharField(max_length=30, null=True, verbose_name='About Content 2 SubTitle')),
                ('subtitle_ru', models.CharField(max_length=30, null=True, verbose_name='About Content 2 SubTitle')),
                ('subtitle_en', models.CharField(max_length=30, null=True, verbose_name='About Content 2 SubTitle')),
            ],
        ),
        migrations.CreateModel(
            name='AboutTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=20, verbose_name='About Title 1')),
                ('title1_hy', models.CharField(max_length=20, null=True, verbose_name='About Title 1')),
                ('title1_ru', models.CharField(max_length=20, null=True, verbose_name='About Title 1')),
                ('title1_en', models.CharField(max_length=20, null=True, verbose_name='About Title 1')),
                ('title2', models.CharField(max_length=20, verbose_name='About Title 2')),
                ('title2_hy', models.CharField(max_length=20, null=True, verbose_name='About Title 2')),
                ('title2_ru', models.CharField(max_length=20, null=True, verbose_name='About Title 2')),
                ('title2_en', models.CharField(max_length=20, null=True, verbose_name='About Title 2')),
                ('text', models.TextField(verbose_name='About Title Text')),
                ('text_hy', models.TextField(null=True, verbose_name='About Title Text')),
                ('text_ru', models.TextField(null=True, verbose_name='About Title Text')),
                ('text_en', models.TextField(null=True, verbose_name='About Title Text')),
            ],
            options={
                'verbose_name': 'AboutTitle',
                'verbose_name_plural': 'AboutTitle',
            },
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name': 'Footer', 'verbose_name_plural': 'Footer'},
        ),
    ]
