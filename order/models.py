from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from property.models import Property as myProperty


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    myproperty = models.ForeignKey(myProperty, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.myproperty.title

    @property
    def amount(self):
        return self.quantity * self.myproperty.price

    @property
    def price(self):
        return self.myproperty.price

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']