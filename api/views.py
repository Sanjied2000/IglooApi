from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from api.serializers import icecreamSerializer,FavouriteSerializer,OrderSerializer,PaymentSerializer
from .models import IceCream,Favourite,Order,Payment
from api.permissions import IsAccountAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated


class IceCreamViewSet(viewsets.ModelViewSet):
    queryset = IceCream.objects.all()
    serializer_class = icecreamSerializer
    permission_classes = [IsAccountAdminOrReadOnly]

class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    lookup_field = 'user__username'
class OrderViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  
            return Order.objects.all()
        return Order.objects.filter(user=user)  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    serializer_class = OrderSerializer
    lookup_field = 'user__username'
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = 'order_id'
    permission_classes = [IsAuthenticated]


    
