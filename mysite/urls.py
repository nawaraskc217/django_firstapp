
from django.contrib import admin
from django.urls import path,include


##main URL
urlpatterns = [
    path('admin/', admin.site.urls),
     path('food/', include('food.urls')), ## food folder->urls, 'food/'-> is url
      path('show/', include('food.urls')),
]
