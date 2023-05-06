from django.db import models

# Create your models here.

class Header(models.Model):

    img = models.ImageField('Header Logo Image', upload_to='images')
    path1 = models.CharField('Header Path 1', max_length=25)
    path2 = models.CharField('Header Path 2', max_length=25)
    path3 = models.CharField('Header Path 3', max_length=25)
    path4 = models.CharField('Header Path 4', max_length=25)
    path5 = models.CharField('Header Path 5', max_length=25)

    class Meta:

        verbose_name = 'Header'
        verbose_name_plural = 'Header'

class HomeTitle(models.Model):

    img = models.ImageField('Header Image', upload_to='images')
    title = models.CharField('Header Title', max_length=30)
    subtitle = models.CharField('Header SubTitle', max_length=50)
    btn_name = models.CharField('Header Button Name', max_length=25)

    class Meta:

        verbose_name = 'HomeTitle'
        verbose_name_plural = 'HomeTitle'

class HomePageLeftContent(models.Model):

    title1 = models.CharField('Home Page Left Content Title 1', max_length=40)
    title2 = models.CharField('Home Page Left Content Title 2', max_length=40)
    img = models.ImageField('Home Page Image', upload_to='images')

    class Meta:

        verbose_name = 'HomePageLeftContent'
        verbose_name_plural = 'HomePageLeftContent'

class HomePageRightContent(models.Model):

    title = models.CharField('Home Page Right Content Title', max_length=40)
    date = models.CharField('Home Page Right Content Date', max_length=40)
    location = models.CharField('Home Page Right Content Location', max_length=40)
    subtitle = models.CharField('Home Page Right Content SubTitle', max_length=40)
    text = models.TextField('Home Page Right Content Text')
    
    class Meta:

        verbose_name = 'HomePagRightContent'
        verbose_name_plural = 'HomePagRightContent'

class HomePageContent2(models.Model):

    title1 = models.CharField('Home Page Content2 Title 1', max_length=40)
    title2 = models.CharField('Home Page Content2 Title 2', max_length=40)
    text = models.TextField('Home Page Content2 Text')
    btn_name = models.CharField('Home Page Content2 Button Name', max_length=25)
    img = models.ImageField('Home Page Content2 Image', upload_to='images')

    class Meta:

        verbose_name = 'HomePageContent2'
        verbose_name_plural = 'HomePageContent2'

class HomeContactGet(models.Model):

    title1 = models.CharField('Home ContactGet Title 1', max_length=40)
    title2 = models.CharField('Home ContactGet Title 2', max_length=40)
    name = models.CharField('Home ContactGet Name', max_length=30)
    surname = models.CharField('Home ContactGet Surname', max_length=30)
    email = models.CharField('Home ContactGet Email', max_length=30)
    subject = models.CharField('Home ContactGet Subject', max_length=30)
    message = models.CharField('Home ContactGet Message', max_length=30)
    btn_name = models.CharField('Home ContactGet Button', max_length=30)
    img = models.ImageField('Home ContactGet Image', upload_to='images')

    class Meta:

        verbose_name = 'HomeContactGet'
        verbose_name_plural = 'HomeContactGet'

class HomeContactPost(models.Model):

    user_name = models.CharField('User Name', max_length=40)
    user_surname = models.CharField('User Surname', max_length=40)
    user_email = models.EmailField('User Email')
    user_subject = models.CharField('User Subject', max_length=50)
    user_message = models.TextField('User Message')

    def __str__(self) -> str:
        return self.user_name

class Footer(models.Model):

    img = models.ImageField('Footer Logo Image', upload_to='images')
    text = models.TextField('Footer Text')
    copyright1 = models.CharField('Footer Copyright', max_length=70)
    design = models.CharField('Footer Design', max_length=40)
    title1 = models.CharField('Footer Title 1', max_length=40)
    title2 = models.CharField('Footer Title 2', max_length=40)
    title3 = models.CharField('Footer Title 3', max_length=40)
    title4 = models.CharField('Footer Title 4', max_length=40)
    subtitle1 = models.CharField('Footer SubTitle 1', max_length=40)
    subtitle2 = models.CharField('Footer SubTitle 2', max_length=40)
    subtitle3 = models.CharField('Footer SubTitle 3', max_length=40)
    subtitle4 = models.CharField('Footer SubTitle 4', max_length=40)
    subtitle5 = models.CharField('Footer SubTitle 5', max_length=40)
    subtitle6 = models.CharField('Footer SubTitle 6', max_length=40)
    subtitle7 = models.CharField('Footer SubTitle 7', max_length=40)
    subtitle8 = models.CharField('Footer SubTitle 8', max_length=40)
    subtitle9 = models.CharField('Footer SubTitle 9', max_length=40)
    social1 = models.CharField('Footer Social 1', max_length=30)
    social2 = models.CharField('Footer Social 2', max_length=30)
    social3 = models.CharField('Footer Social 3', max_length=30)
    social_url1 = models.URLField('Footer Social URL1')
    social_url2 = models.URLField('Footer Social URL2')
    social_url3 = models.URLField('Footer Social URL3')
    placeholder = models.CharField('Footer PlaceHolder', max_length=30)
    btn_name = models.CharField('Footer Button Name', max_length=30)
    go_to_top = models.CharField('Footer Go to Top', max_length=30)

    class Meta:

        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'

class AboutTitle(models.Model):

    title1 = models.CharField('About Title 1', max_length=20)
    title2 = models.CharField('About Title 2', max_length=20)
    text = models.TextField('About Title Text')

    class Meta:

        verbose_name = 'AboutTitle'
        verbose_name_plural = 'AboutTitle'

class AboutContent(models.Model):

    title1 = models.CharField('About Content Title', max_length=30)
    title2 = models.CharField('About Content Title', max_length=30)
    title3 = models.CharField('About Content Title', max_length=30)

class AboutContent2(models.Model):

    title1 = models.CharField('About Content 2 Title 1', max_length=30)
    title2 = models.CharField('About Content 2 Title 2', max_length=30)
    img = models.ImageField('About Content Image', upload_to='images')
    text1 = models.TextField('About Text 1')
    text2 = models.TextField('About Text 2')
    subtitle = models.CharField('About Content 2 SubTitle', max_length=30)
    
    class Meta:

        verbose_name = 'AboutContents2'
        verbose_name_plural = 'AboutContents2'

class AboutContent2Info(models.Model):

    title1 = models.CharField('About Content2 Info Title 1', max_length=40)
    title2 = models.CharField('About Content2 Info Title 2', max_length=40)
    title3 = models.CharField('About Content2 Info Title 3', max_length=40)
    text1 = models.TextField('About Content 2 Info Text 1')
    text2 = models.TextField('About Content 2 Info Text 2')
    text3 = models.TextField('About Content 2 Info Text 3')

class AboutLastContent(models.Model):

    title = models.CharField('About Last Content Title', max_length=60)
    btn_name = models.CharField('About Last Content Button Name', max_length=30)

class ExploreTitle(models.Model):

    title1 = models.CharField('Explore Title 1', max_length=20)
    title2 = models.CharField('Explore Title 2', max_length=20)
    text = models.TextField('Explore Text')
    
    class Meta:

        verbose_name = 'ExploreTitle'
        verbose_name_plural = 'ExploreTitle'

class ExploreContent(models.Model):

    title = models.CharField('Explore Content Title', max_length=80)
    img = models.ImageField('Explore Content Image', upload_to='images')

class ExploreContentList(models.Model):

    title = models.CharField('Explore Content List Title', max_length=30)
    subtitle = models.CharField('Explore Content List SubTitle', max_length=30)

class ExploreContent2(models.Model):

    text1 = models.TextField('Explore Content 2 Text 1')
    text2 = models.TextField('Explore Content 2 Text 2')
    img1 = models.ImageField('Explore Content 2 Image 1', upload_to='images')
    img2 = models.ImageField('Explore Content 2 Image 2', upload_to='images')
    title = models.CharField('Explore Content 2 Title', max_length=40)
    text3 = models.TextField('Explore Content 2 Text 3')
    left_img = models.ImageField('Explore Content 2 Left Image', upload_to='images')
    left_title = models.CharField('Explore Content 2 Left Title', max_length=60)
    left_subtitle = models.CharField('Explore Content 2 Left SubTitle', max_length=50)
    right_img = models.ImageField('Explore Content 2 Right Image', upload_to='images')
    right_title = models.CharField('Explore Content 2 Right Title', max_length=60)
    right_subtitle = models.CharField('Explore Content 2 Right SubTitle', max_length=50)

    class Meta:

        verbose_name = 'ExploreContent2'
        verbose_name_plural = 'ExploreContent2'


class ExploreLastContent(models.Model):

    title = models.CharField('Explore Last Content Title', max_length=60)
    btn_name = models.CharField('Explore Last Content Button Name', max_length=30)

    class Meta:

        verbose_name = 'ExploreLastContent'
        verbose_name_plural = 'ExploreLastContent'

class TrendingTitle(models.Model):

    title1 = models.CharField('Trending Title 1', max_length=20)
    title2 = models.CharField('Trending Title 2', max_length=20)
    text = models.TextField('Trending Text')

    class Meta:

        verbose_name = 'TrendingTitle'
        verbose_name_plural = 'TrendingTitle'

class TrendingContentList(models.Model):

    title = models.CharField('Trending Content List Title', max_length=30)
    subtitle = models.CharField('Trending Content List Subtitle', max_length=50)
    img = models.ImageField('Trending Content List Image', upload_to='images')

class TrendingLastContent(models.Model):

    title = models.CharField('Trending Last Content Title', max_length=80)
    btn_name = models.CharField('Trending Last Content Button Name', max_length=40)

    class Meta:

        verbose_name = 'TrendingLastContent'
        verbose_name_plural = 'TrendingLastContent'

class ContactTitle(models.Model):

    title1 = models.CharField('Contact Title 1', max_length=20)
    title2 = models.CharField('Contact Title 2', max_length=20)
    text = models.TextField('Contact Text')

    class Meta:

        verbose_name = 'ContactTitle'
        verbose_name_plural = 'ContactTitle'

class ContactGet(models.Model):

    subtitle1 = models.CharField('Contact Get SubTitle 1', max_length=40)
    subtitle2 = models.CharField('Contact Get SubTitle 2', max_length=40)
    subtitle3 = models.CharField('Contact Get SubTitle 3', max_length=40)
    info1 = models.CharField('Contact Get Info 1', max_length=60)
    info2 = models.CharField('Contact Get Info 2', max_length=60)
    info3 = models.CharField('Contact Get Info 3', max_length=60)

    class Meta:

        verbose_name = 'ContactGet'
        verbose_name_plural = 'ContactGet'

class ContactPost(models.Model):

    user_name = models.CharField('User Name', max_length=40)
    user_surname = models.CharField('User Surname', max_length=40)
    user_email = models.EmailField('User Email')
    user_subject = models.CharField('User Subject', max_length=50)
    user_message = models.TextField('User Message')

    def __str__(self) -> str:
        return self.user_name