from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound

from .models import Product

@api_view(['POST'])
def product_create(request):
    title = request.data.get('title')
    desc = request.data.get('desc')
    price = request.data.get('price')

    product = Product(title=title, desc=desc, price=price) #.objects.create qilsak ham bo'ladi
    product.save()

    return Response(
        {'msg': 'Product created successfully', 
         'title':product.title,
         'desc':product.desc,
         'price':product.price,
         },
        status=status.HTTP_201_CREATED
    )

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all() # query_set da [obj1, obj2, obj3]
    product_list = []

    for product in products:
        product_list.append({
            'id':product.id,
            'title':product.title,
            'desc':product.desc,
            'price':product.price
        })

    return Response({
        'msg': 'Product list fetched successfully',
        'count': len(product_list),
        'products':product_list}, status=status.HTTP_200_OK)

@api_view(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'msg': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    product_data = {
        'id':product.id,
        'title':product.title,
        'desc':product.desc,
        'price':product.price
    }

    return Response({
        'msg': 'Product detail fetched successfully',
        'product':product_data
    }, status=status.HTTP_200_OK)

@api_view(['PUT'])
def product_update(request, pk):
    product = Product.objects.filter(pk=pk).first()

    if not product:
        raise NotFound('Product not found')

    product.title = request.data.get('title')
    product.desc = request.data.get('desc')
    product.price = request.data.get('price')

    product.save()

    return Response({
        'msg': 'Product updated', 
        'title':product.title,
        'desc':product.desc,
        'price':product.price,
    }, status=status.HTTP_200_OK)

