from django.shortcuts import render
from django.http import JsonResponse

# This view just returns a json data of routes, the safe=False we can return any kind of data to json response as this is just a python list here
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
    return JsonResponse(routes, safe=False)

# At this point we have just built a simplified api that returns a json response, but if we continue like this it would be a pain in the ass as we would have to manually do stuffs like serialization of our python object so we would use django rest framework
# In other to render routes out we need to do data serialization that would convert our python object to a json data and then we render it out
