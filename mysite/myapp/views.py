from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.

def index(request):
    context = {
        "items" : Product.objects.all()
        }
    
    return render(request, "myapp\index.html", context)

def indexItem(request, my_id):
    item = Product.objects.get(id=my_id)
    context = {
        'item':item
    }
    return render(request, "myapp\detail.html", context)


