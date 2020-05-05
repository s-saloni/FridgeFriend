from django.urls import path, include

#from django.contrib import admin

#admin.autodiscover()


import hello.views
import recipes.views

urlpatterns = [
    path("", hello.views.main, name="main"),
    path("recipes/", include("recipes.urls")),
    path('pantry/', include('pantry.urls')),
    path("account/", hello.views.account, name="account"),
    path("contactus/", hello.views.contactus, name="contactus"),
    path("shoppinglist/", hello.views.shoppinglist, name="shoppinglist"),
    path("recipes-result/", recipes.views.search_recipes, name="search_recipes"),
]
