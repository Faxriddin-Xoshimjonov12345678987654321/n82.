from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product

@api_view(['POST'])
def product_create(request):
    title = request.data.get('title')
    desc = request.data.get('desc')
    price = request.data.get('price')

    product = Product(title=title, desc=desc, price=price) #.objects.create qilsak ham bo'ladi
    product.save()

    return Response(
        {
            'msg': 'Product created',
            'status': status.HTTP_201_CREATED
        }
    )