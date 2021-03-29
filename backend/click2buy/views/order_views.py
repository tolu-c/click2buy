from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# from django.core.paginator import Paginator, EmptyP?age, PageNotAnInteger

from click2buy.models import Product, Order, OrderItem, ShippingAddress
from click2buy.serializer import ProductSerializer

from rest_framework import status


@api_view('POST')
@permission_classes(['IsAuthenticated'])
def addOrderItems(request):
    
    user = request.user
    data = request.data
    
    orderItems = data['orderItems']
    
    if orderItems and len(orderItems) == 0:
        return Response({'detail':'No Order Items', status=status.HTTP_400})
    
    return Response('ORDER')
