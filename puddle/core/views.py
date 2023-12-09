from django.shortcuts import render

from item.models import Category, Item

def index(request):
    itens = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categorys': categories,
        'itens': itens,
    })

def contact(request):
    return render(request, 'core/contact.html')


