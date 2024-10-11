from . import views 
from django.urls import path,include


urlpatterns = [

        path('',views.index,name='index'),##connects to views.py and index() function
         path('',views.show,name='show') ##connects to views.py and show() function
         
]