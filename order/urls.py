from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('orderproperty/', views.orderproperty, name='orderproperty'),

]