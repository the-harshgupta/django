from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello Python3 with Django Server")
    people = [
        {'name' : 'Harsh Gupta','age' : 20},
        {'name' : 'Pranay ','age' : 15},
    ]
    vegetable = ['Potato','Tomato','Onion']
    return render(request, "index.html", context = {'people' : people ,'vegetable ':vegetable} )
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, "contact.html")

