from rest_framework import serializers
from .models import IceCream,Favourite,Order,Payment
from django.contrib.auth.models import User



class icecreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class FavouriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    ) 
    icecream =icecreamSerializer()
    class Meta:
        model = Favourite
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    ) 
    icecream =icecreamSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderShortSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )     
    class Meta:
        model = Order
        fields = ['id','user','orderdate']


class PaymentSerializer(serializers.ModelSerializer):

    order = OrderShortSerializer(read_only=True)
    class Meta:
        model = Payment
        fields = "__all__"