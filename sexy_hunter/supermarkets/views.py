from django.shortcuts import render, redirect
from django.http import HttpResponse
from supermarkets.models import Item, Supermarket


def supermarket_list(request):
    all_of_the_items = Item.objects.order_by('supermarket')  
    all_of_them = Supermarket.objects.all()
    return render(request, 'home.html', {'supermarkets' : all_of_them})

def add_supermarket(request):
    Supermarket.objects.create(
            super_name = request.POST.get('supermarket_name'), 
            opening_hours = request.POST.get('opening_hours'))
    return redirect('/')
# Create your views here.
