from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.

#Recipes Page
def recipes(request):
    return render(request, "recipes.html")

#Pantry Page
def pantry(request):
    return render(request, "pantry.html")

#Main landing page
def main(request):
    return render(request, "main.html")

def account(request):
    return render(request, "account.html")

def contactus(request):
    return render(request, "contactus.html")

def shoppinglist(request):
    return render(request, "shoppinglist.html")
