from django.urls import path

from .views import *

urlpatterns = [
    path('create/', product_create),
    path('list/', product_list),
    path('detail/<int:id>/', product_detail),
]