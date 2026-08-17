from django.urls import path

from .views import *

urlpatterns = [
    path('create/', product_create),
    path('list/', product_list),
    path('detail/<int:pk>/', product_detail),   
    path('update/<int:pk>/', product_update),   
    path('partila_update/<int:pk>/', product_partial_update),   
    path('delete/<int:pk>/', product_delete),   
]