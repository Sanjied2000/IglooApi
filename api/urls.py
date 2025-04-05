
from django.contrib import admin
from django.urls import path,include
from .views import IceCreamViewSet,FavouriteViewSet,OrderViewSet,PaymentViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'icecream', IceCreamViewSet)
router.register(r'favourite', FavouriteViewSet)
router.register(r'order', OrderViewSet,basename='order')
router.register(r'payment', PaymentViewSet)


urlpatterns = [
    
    path('', include(router.urls))
    
]

