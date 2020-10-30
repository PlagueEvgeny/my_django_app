from django.shortcuts import render

from mainapp.models import SubjectCategory, Course

def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = SubjectCategory.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }

    return render(request, 'mainapp/catalog.html', context)

def basket(request):
    return render(request, 'mainapp/basket.html')

def catalog_page(request, pk):
    courses = Course.objects.filter(category_id=pk)
    context = {
        'courses': courses,
        'page_title': 'страница каталога'
    }
    return render(request, 'mainapp/catalog_page.html', context)