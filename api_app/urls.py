from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    #############################################################################
    ################################## PRODUCT URL ##############################
    #############################################################################
    path('products/', views.getProducts),
    path('products/create/', views.createProduct), # Make sure this comes before getProduct because the url is expecting a primary key and it will give error that create was passed if we visit this url
    path('products/<str:pk>/', views.getProduct),
    path('products/<str:pk>/update/', views.updateProduct),
    path('products/<str:pk>/delete/', views.deleteProduct),


    #############################################################################
    ################################## ORDER URL ################################
    #############################################################################
    path('order/create/', views.createOrder),
    path('order/<str:pk>/update/', views.updateOrder),


    #############################################################################
    ################################## ORDER ITEM URL ###########################
    #############################################################################
    path('order_item/<str:order>/create/', views.createOrderItem),
    path('order_item/<str:pk>/update/', views.updateOrderItem),
    path('order_item/<str:pk>/delete/', views.deleteOrderItem),
]