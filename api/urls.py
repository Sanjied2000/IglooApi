
from django.contrib import admin
from django.urls import path,include
from .views import IceCreamViewSet,FavouriteViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'icecream', IceCreamViewSet)
router.register(r'favourite', FavouriteViewSet)


urlpatterns = [
    
    path('', include(router.urls))
    
]

