from django.shortcuts import render, redirect
from django.http import HttpResponse
from supermarkets.models import Item, Supermarket


def supermarket_list(request):
    all_of_them = Supermarket.objects.all()
    all_of_items = Item.objects.all()
    return render(request, 'home.html', {'supermarkets' : all_of_them,
                                         'items' : all_of_items})

def add_supermarket(request):
    Supermarket.objects.create(
            super_name = request.POST.get('supermarket_name'), 
            opening_hours = request.POST.get('opening_hours'))
    return redirect('/')

def add_item(request):
    super_name = request.POST.get('supermarket')
    Item.objects.create(
        supermarket =
        Supermarket.objects.get(super_name=super_name),
        i_name = request.POST.get('item_name'),
        price = request.POST.get('item_price'),
        category = request.POST.get('category'),
    )
    return redirect('/supermarkets/%s/'%  super_name)

# this returns a page with the supermarket and all of its items
def current_supermarket(request, anyname):
    supermarket = Supermarket.objects.get(super_name=anyname)
    items = Item.objects.filter(supermarket=supermarket)
    return render(request, 'market.html', {'supermarket' : supermarket,
                                           'items' : items}) 

def add_supermarket_page(request):
    return render(request, 'add_supermarket.html')

