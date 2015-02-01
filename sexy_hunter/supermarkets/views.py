from django.shortcuts import render
from django.http import HttpResponse
from supermarkets.models import Item


def supermarket_list(request):
    all_of_the_items = Item.objects.order_by('supermarket')  
    return render(request, 'home.html', { all_of_the_items : 'items'})

def add_supermarket(request):
    new_market_name = request.POST['supermarket_name']
    new_market_opening_hours = request.POST['opening_hours']
    supermarket = Supermarket.objects.create(new_market_opening_hours, new_market_name)
    return render(request, 'add_supermarket.html',)
# Create your views here.
