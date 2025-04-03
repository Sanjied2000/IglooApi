from django.db import models
from django.contrib.auth.models import User

class IceCream(models.Model):
    icecreamName =models.CharField(max_length=20)
    flavour =models.CharField(max_length=20)
    type =models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.icecreamName
    
class Favourite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icecream= models.ForeignKey(IceCream,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.icecream.icecreamName}"


