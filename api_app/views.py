from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer
from .models import Product, Order, OrderItem
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/products/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of products'
        },
        {
            'Endpoint':'/products/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single product object'
        },
        {
            'Endpoint':'/products/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates new product with data sent in post request'
        },
        {
            'Endpoint':'/products/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'description':'Updates an existing product with data sent in'
        },
        {
            'Endpoint':'/products/id/delete/',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an existing product'
        },
    ]
    return Response(routes)

# In other to render routes out we need to do data serialization that would convert our python/django objects to a json data and then we render it out

#############################################################################
################################## PRODUCT ENDPOINT #########################
#############################################################################
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    # product = Product.objects.get(id=pk)
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    data = request.data
    product = Product.objects.create(
        name = data['name'],
        price = data['price'],
        description = data['description'],
        image = data['image']

    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def updateProduct(request, pk):
    data = request.data
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteProduct(request, pk):
    # product = Product.objects.get(id=pk)
    product = get_object_or_404(Product, id=pk)
    product.delete()
    return Response('Product was deleted')

#############################################################################
################################## ORDER ENDPOINT ###########################
#############################################################################
@api_view(['POST'])
def createOrder(request):
    data = request.data
    print(f"Data: {data}, DataType: {type(data)}")
    order = Order.objects.create(
        date_orderd = data['date_ordered'],
        transaction_id = data['transaction_id'],
        complete = data['complete']
    )
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateOrder(request, pk):
    order = get_object_or_404(Order, id=pk)
    serializer = OrderSerializer(order, data=request.data)
    print(f"Data 1: {order}")
    if serializer.is_valid():
        serializer.save()
        print(f"Data 2: {serializer.data}")
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#############################################################################
################################## ORDER ITEM ENDPOINT ######################
#############################################################################
@api_view(['POST'])
def createOrderItem(request, order):
    data = request.data
    print(f"Data: {data}")
    order = get_object_or_404(Order, id=order)
    orderItem = OrderItem.objects.create(
        product = get_object_or_404(Product, name=data['product']),
        order = get_object_or_404(Order, transaction_id=data['order']),
        quantity = data['quantity'],
        date_added = data['date_added']
    )
    serializer = OrderItemSerializer(orderItem, many=False)
    return Response(serializer.data)

# @api_view(['PUT'])
# def updateOrderItem(request, pk):
#     data = request.data
#     print(f"Data 1: {data}")
#     orderItem = get_object_or_404(OrderItem, id=pk)
#     serializer = OrderItemSerializer(orderItem, data={'product': get_object_or_404(Product, name=data['product']), 'order': get_object_or_404(Order, id=data['order']), 'quantity': '790', 'date_added': data['date_added']})
#     if serializer.is_valid():
#         serializer.save()
#         print(f"Data 2: {serializer.data}")
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateOrderItem(request, pk):
    data = request.data
    print(f"Data 1: {data}")
    
    try:
        orderItem = get_object_or_404(OrderItem, id=pk)
        product = get_object_or_404(Product, name=data['product'])
        order = get_object_or_404(Order, id=data['order'])
        
        serializer = OrderItemSerializer(orderItem, data={
            'product': product.id,
            'order': order.id,
            'quantity': data['quantity'],
            'date_added': data['date_added']
        }, partial=True)  # Use partial=True to allow partial updates
        
        if serializer.is_valid():
            serializer.save()
            print(f"Data 2: {serializer.data}")
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except KeyError as e:
        return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def deleteOrderItem(request, pk):
    orderItem = get_object_or_404(OrderItem, id=pk)
    orderItem.delete()
    return Response('Product was deleted')