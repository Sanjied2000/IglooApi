from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from api.serializers import icecreamSerializer,FavouriteSerializer
from .models import IceCream,Favourite
from rest_framework.response import Response
from api.permissions import IsAccountAdminOrReadOnly


class IceCreamViewSet(viewsets.ModelViewSet):
    queryset = IceCream.objects.all()
    serializer_class = icecreamSerializer
    permission_classes = [IsAccountAdminOrReadOnly]

class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    lookup_field = 'user__username'
    
