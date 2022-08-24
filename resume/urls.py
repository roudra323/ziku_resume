from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contract', views.contract, name='contract'),
    path('serv/', include('serv.urls')),
    path('edu/', include('edu.urls')),
]
