from .models import Header, HomeTitle, HomePageLeftContent, HomePageRightContent, HomePageContent2, HomeContactGet, Footer
from .models import AboutTitle, AboutContent, AboutContent2, AboutContent2Info, AboutLastContent
from .models import ExploreTitle, ExploreContent, ExploreContentList, ExploreContent2, ExploreLastContent
from .models import TrendingTitle, TrendingLastContent
from .models import ContactTitle, ContactGet
from modeltranslation.translator import register, TranslationOptions

@register(Header)
class HeaderTranslationOptions(TranslationOptions):
    fields = ('path1', 'path2', 'path3', 'path4', 'path5',)

@register(HomeTitle)
class HomeTitleTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'btn_name',)

@register(HomePageLeftContent)
class HomePageLeftContentTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2',)

@register(HomePageRightContent)
class HomePageRightContentTranslationOptions(TranslationOptions):
    fields = ('title', 'date', 'location', 'subtitle', 'text',)

@register(HomePageContent2)
class HomePageContent2TranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'text', 'btn_name',)

@register(HomeContactGet)
class HomeContactGetTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'name', 'surname', 'email', 'subject', 'message', 'btn_name',)

@register(Footer)
class FooterTranslationOptions(TranslationOptions):
    fields = ('text', 'title1', 'title2', 'title3', 'title4', 'placeholder', 'btn_name', 'go_to_top',)

@register(AboutTitle)
class AboutTitleTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'text',)

@register(AboutContent)
class AboutContentTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'title3',)

@register(AboutContent2)
class AboutContent2TranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'text1', 'text2', 'subtitle',)

@register(AboutContent2Info)
class AboutContent2InfoTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'title3', 'text1', 'text2', 'text3',)

@register(AboutLastContent)
class AboutLastContentTranslationOptions(TranslationOptions):
    fields = ('title', 'btn_name',)

@register(ExploreTitle)
class ExploreTitleTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'text',)

@register(ExploreContent)
class ExploreContentTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ExploreContentList)
class ExploreContentListTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',)

@register(ExploreContent2)
class ExploreContent2TranslationOptions(TranslationOptions):
    fields = ('text1', 'text2', 'title', 'text3', 'left_title', 'left_subtitle', 'right_title', 'right_subtitle',)

@register(ExploreLastContent)
class ExploreLastContentTranslationOptions(TranslationOptions):
    fields = ('title', 'btn_name',)

@register(TrendingTitle)
class TrendingTitleTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'text')

@register(TrendingLastContent)
class TrendingLastContentTranslationOptions(TranslationOptions):
    fields = ('title', 'btn_name',)

@register(ContactTitle)
class ContactGetTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'text',)

@register(ContactGet)
class ContactGetTranslationOptions(TranslationOptions):
    fields = ('subtitle1', 'subtitle2', 'subtitle3', 'info1',)