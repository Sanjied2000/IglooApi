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
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    icecream= models.ManyToManyField(IceCream)
    orderdate = models.DateField(auto_now_add=True) 

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_status=models.BooleanField(default=False)
    def __str__(self):
        return f"Payment for Order #{self.order.id} - {'Paid' if self.payment_status else 'Pending'}"
    



    



