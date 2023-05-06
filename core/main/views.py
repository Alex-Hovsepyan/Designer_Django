from django.shortcuts import render, redirect
from .models import Header, HomeTitle, HomePageLeftContent, HomePageRightContent, HomePageContent2, HomeContactGet, HomeContactPost, Footer
from .models import AboutTitle, AboutContent, AboutContent2, AboutContent2Info, AboutLastContent
from .models import ExploreTitle, ExploreContent, ExploreContentList, ExploreContent2, ExploreLastContent
from .models import TrendingTitle, TrendingContentList, TrendingLastContent
from .models import ContactTitle, ContactGet, ContactPost
from .forms import ContactModelForm, ContactModelForm2

# Create your views here.

def double_content():
    header = Header.objects.all()[0]
    home_title = HomeTitle.objects.all()[0]
    footer = Footer.objects.all()[0]
    return [header, home_title, footer]

def index(request):
    home_page_left_content = HomePageLeftContent.objects.all()[0]
    home_page_right_content = HomePageRightContent.objects.all()
    home_page_content2 = HomePageContent2.objects.all()[0]
    home_contact_get = HomeContactGet.objects.all()[0]
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            HomeContactPost.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactModelForm()

    return render(request, 'main/index.html', context={
        'header':double_content()[0],
        'home_title':double_content()[1],
        'home_page_left_content':home_page_left_content,
        'home_page_right_content':home_page_right_content,
        'home_page_content2':home_page_content2,
        'home_contact_get':home_contact_get,
        'form':form,
        'footer':double_content()[2],

    })

def about(request):
    about_title = AboutTitle.objects.all()[0]
    about_content = AboutContent.objects.all()[0]
    about_content2 = AboutContent2.objects.all()[0]
    about_content2_info = AboutContent2Info.objects.all()[0]
    about_last_content = AboutLastContent.objects.all()[0]
    return render(request, 'main/about.html', context={
        'header':double_content()[0],
        'home_title':double_content()[1],
        'footer':double_content()[2],
        'about_title':about_title,
        'about_content':about_content,
        'about_content2':about_content2,
        'about_content2_info':about_content2_info,
        'about_last_content':about_last_content,
    })

def explore(request):
    explore_title = ExploreTitle.objects.all()[0]
    explore_content = ExploreContent.objects.all()[0]
    explore_content_list = ExploreContentList.objects.all()
    explore_content2 = ExploreContent2.objects.all()[0]
    explore_last_content = ExploreLastContent.objects.all()[0]
    return render(request, 'main/explore.html', context={
        'header':double_content()[0],
        'home_title':double_content()[1],
        'footer':double_content()[2],
        'explore_title':explore_title,
        'explore_content':explore_content,
        'explore_content_list':explore_content_list,
        'explore_content2':explore_content2,
        'explore_last_content':explore_last_content,
    })

def trending(request):
    trending_title = TrendingTitle.objects.all()[0]
    trending_content_list = TrendingContentList.objects.all()
    trending_last_content = TrendingLastContent.objects.all()[0]
    return render(request, 'main/trending.html', context={
        'header':double_content()[0],
        'home_title':double_content()[1],
        'footer':double_content()[2],
        'trending_title':trending_title,
        'trending_content_list':trending_content_list,
        'trending_last_content':trending_last_content,
    })

def contact(request):
    contact_title = ContactTitle.objects.all()[0]
    contact_get = ContactGet.objects.all()[0]
    home_contact_get = HomeContactGet.objects.all()[0]
    trending_last_content = TrendingLastContent.objects.all()[0]
    if request.method == 'POST':
        form = ContactModelForm2(request.POST)
        if form.is_valid():
            ContactPost.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactModelForm2()
    return render(request, 'main/contact.html', context={
        'header':double_content()[0],
        'home_title':double_content()[1],
        'footer':double_content()[2],
        'contact_title':contact_title,
        'contact_get':contact_get,
        'home_contact_get':home_contact_get,
        'trending_last_content':trending_last_content,
    })