from rest_framework import serializers
from .models import IceCream,Favourite
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
 