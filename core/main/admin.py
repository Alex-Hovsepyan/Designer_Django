from django.contrib import admin
from .models import Header, HomeTitle, HomePageLeftContent, HomePageRightContent, HomePageContent2, HomeContactGet, HomeContactPost, Footer
from .models import AboutTitle, AboutContent, AboutContent2, AboutContent2Info, AboutLastContent
from .models import ExploreTitle, ExploreContent, ExploreContentList, ExploreContent2, ExploreLastContent
from .models import TrendingTitle, TrendingContentList, TrendingLastContent
from .models import ContactTitle, ContactGet, ContactPost
from modeltranslation.admin import TranslationAdmin

class HeaderAdmin(TranslationAdmin): 
    pass

admin.site.register(Header)
admin.site.register(HomeTitle)
admin.site.register(HomePageLeftContent)
admin.site.register(HomePageRightContent)
admin.site.register(HomePageContent2)
admin.site.register(HomeContactGet)
admin.site.register(HomeContactPost)
admin.site.register(Footer)
admin.site.register(AboutTitle)
admin.site.register(AboutContent)
admin.site.register(AboutContent2)
admin.site.register(AboutContent2Info)
admin.site.register(AboutLastContent)
admin.site.register(ExploreTitle)
admin.site.register(ExploreContent)
admin.site.register(ExploreContentList)
admin.site.register(ExploreContent2)
admin.site.register(ExploreLastContent)
admin.site.register(TrendingTitle)
admin.site.register(TrendingContentList)
admin.site.register(TrendingLastContent)
admin.site.register(ContactTitle)
admin.site.register(ContactGet)
admin.site.register(ContactPost)