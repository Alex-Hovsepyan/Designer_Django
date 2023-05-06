# Generated by Django 4.2 on 2023-04-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_homecontactget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Footer Logo Image')),
                ('text', models.TextField(verbose_name='Footer Text')),
                ('text_hy', models.TextField(null=True, verbose_name='Footer Text')),
                ('text_ru', models.TextField(null=True, verbose_name='Footer Text')),
                ('text_en', models.TextField(null=True, verbose_name='Footer Text')),
                ('copyright1', models.CharField(max_length=70, verbose_name='Footer Copyright')),
                ('design', models.CharField(max_length=40, verbose_name='Footer Design')),
                ('title1', models.CharField(max_length=40, verbose_name='Footer Title 1')),
                ('title1_hy', models.CharField(max_length=40, null=True, verbose_name='Footer Title 1')),
                ('title1_ru', models.CharField(max_length=40, null=True, verbose_name='Footer Title 1')),
                ('title1_en', models.CharField(max_length=40, null=True, verbose_name='Footer Title 1')),
                ('title2', models.CharField(max_length=40, verbose_name='Footer Title 2')),
                ('title2_hy', models.CharField(max_length=40, null=True, verbose_name='Footer Title 2')),
                ('title2_ru', models.CharField(max_length=40, null=True, verbose_name='Footer Title 2')),
                ('title2_en', models.CharField(max_length=40, null=True, verbose_name='Footer Title 2')),
                ('title3', models.CharField(max_length=40, verbose_name='Footer Title 3')),
                ('title3_hy', models.CharField(max_length=40, null=True, verbose_name='Footer Title 3')),
                ('title3_ru', models.CharField(max_length=40, null=True, verbose_name='Footer Title 3')),
                ('title3_en', models.CharField(max_length=40, null=True, verbose_name='Footer Title 3')),
                ('title4', models.CharField(max_length=40, verbose_name='Footer Title 4')),
                ('title4_hy', models.CharField(max_length=40, null=True, verbose_name='Footer Title 4')),
                ('title4_ru', models.CharField(max_length=40, null=True, verbose_name='Footer Title 4')),
                ('title4_en', models.CharField(max_length=40, null=True, verbose_name='Footer Title 4')),
                ('subtitle1', models.CharField(max_length=40, verbose_name='Footer SubTitle 1')),
                ('subtitle2', models.CharField(max_length=40, verbose_name='Footer SubTitle 2')),
                ('subtitle3', models.CharField(max_length=40, verbose_name='Footer SubTitle 3')),
                ('subtitle4', models.CharField(max_length=40, verbose_name='Footer SubTitle 4')),
                ('subtitle5', models.CharField(max_length=40, verbose_name='Footer SubTitle 5')),
                ('subtitle6', models.CharField(max_length=40, verbose_name='Footer SubTitle 6')),
                ('subtitle7', models.CharField(max_length=40, verbose_name='Footer SubTitle 7')),
                ('subtitle8', models.CharField(max_length=40, verbose_name='Footer SubTitle 8')),
                ('subtitle9', models.CharField(max_length=40, verbose_name='Footer SubTitle 9')),
                ('social1', models.CharField(max_length=30, verbose_name='Footer Social 1')),
                ('social2', models.CharField(max_length=30, verbose_name='Footer Social 2')),
                ('social3', models.CharField(max_length=30, verbose_name='Footer Social 3')),
                ('social_url1', models.URLField(verbose_name='Footer Social URL1')),
                ('social_url2', models.URLField(verbose_name='Footer Social URL2')),
                ('social_url3', models.URLField(verbose_name='Footer Social URL3')),
                ('placeholder', models.CharField(max_length=30, verbose_name='Footer PlaceHolder')),
                ('placeholder_hy', models.CharField(max_length=30, null=True, verbose_name='Footer PlaceHolder')),
                ('placeholder_ru', models.CharField(max_length=30, null=True, verbose_name='Footer PlaceHolder')),
                ('placeholder_en', models.CharField(max_length=30, null=True, verbose_name='Footer PlaceHolder')),
                ('btn_name', models.CharField(max_length=30, verbose_name='Footer Button Name')),
                ('btn_name_hy', models.CharField(max_length=30, null=True, verbose_name='Footer Button Name')),
                ('btn_name_ru', models.CharField(max_length=30, null=True, verbose_name='Footer Button Name')),
                ('btn_name_en', models.CharField(max_length=30, null=True, verbose_name='Footer Button Name')),
                ('go_to_top', models.CharField(max_length=30, verbose_name='Footer Go to Top')),
                ('go_to_top_hy', models.CharField(max_length=30, null=True, verbose_name='Footer Go to Top')),
                ('go_to_top_ru', models.CharField(max_length=30, null=True, verbose_name='Footer Go to Top')),
                ('go_to_top_en', models.CharField(max_length=30, null=True, verbose_name='Footer Go to Top')),
            ],
        ),
        migrations.AlterField(
            model_name='homecontactget',
            name='email',
            field=models.CharField(max_length=30, verbose_name='Home ContactGet Email'),
        ),
        migrations.AlterField(
            model_name='homecontactget',
            name='email_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Home ContactGet Email'),
        ),
        migrations.AlterField(
            model_name='homecontactget',
            name='email_hy',
            field=models.CharField(max_length=30, null=True, verbose_name='Home ContactGet Email'),
        ),
        migrations.AlterField(
            model_name='homecontactget',
            name='email_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Home ContactGet Email'),
        ),
        migrations.AlterField(
            model_name='homecontactget',
            name='message',
            field=models.CharField(max_length=30, verbose_name='Home ContactGet Message'),
        ),
        migrations.AlterField(
            model_name='homecontactget',
            name='message_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Home ContactGet Message'),
        ),
        migrations.AlterField(
            model_name='homecontactget',
            name='message_hy',
            field=models.CharField(max_length=30, null=True, verbose_name='Home ContactGet Message'),
        ),
        migrations.AlterField(
            model_name='homecontactget',
            name='message_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Home ContactGet Message'),
        ),
    ]