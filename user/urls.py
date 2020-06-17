from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('addimage/<int:id>', views.addimage, name='addimage'),
    path('addproperty/', views.addproperty, name='addproperty'),
    path('properties/', views.properties, name='properties'),
    path('propertyedit/<int:id>', views.propertyedit, name='propertyedit'),
    path('propertydelete/<int:id>', views.propertydelete, name='propertydelete'),
]