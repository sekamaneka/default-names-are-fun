from django.shortcuts import render, redirect
from django.http import HttpResponse
from supermarkets.models import Item, Supermarket


def supermarket_list(request):
    #all_of_the_items = Item.objects.order_by('supermarket')  
    all_of_them = Supermarket.objects.all()
    all_of_items = Item.objects.all()
    return render(request, 'home.html', {'supermarkets' : all_of_them,
                                         'items' : all_of_items})

def add_supermarket(request):
    Supermarket.objects.create(
            super_name = request.POST.get('supermarket_name'), 
            opening_hours = request.POST.get('opening_hours'))
    return redirect('/')
# Placeholder view. The items have to be imported from the lists
# i scrape of the supermarket sites
def add_item(request):
    Item.objects.create(
        i_name = request.POST.get('item_name'),
        price = request.POST.get('item_price'),
        category = request.POST.get('category')
    )
    return redirect('/')
        
