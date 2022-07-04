from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from . serializer import ClientSerializer, ClientViewSerializer,CountrySerializer
from . models import Country,Client
from rest_framework.response import Response
from rest_framework import status



'''
This function is for desplaying all clients data
by bring data from database and serializer it in 
serializer.py file and return response data
'''
@api_view(['GET'])
def display_clients(request):
    data=Client.objects.all()                          # Client is a model  
    serilaizer=ClientViewSerializer(data,many=True)    #ClientViewSerializer is a serializer
    return Response(serilaizer.data)




'''
This function is for Adding all client .
by write the data of the new user .
serializer data and  saving it in database
'''
@api_view(['POST'])
def add_client(request):
    data=Client.objects.all()                             # Client is a model                         
    serializer=ClientSerializer(data,data=request.data)   #ClientSerializer is a serializer
    if serializer.is_valid:
        serializer.save
        return Response(serializer.data,status=status.HTTP_201_CREATED)




'''
This function for get specific user 
by bring data from database and serializer it in 
serializer.py file and return response data
'''
@api_view(['GET'])
def display_client(request,id):
    data=Client.objects.get(id=id)                      # Client is a model
    serializer=ClientViewSerializer(data).data          #ClientSerializer is a serializer
    return Response(serializer)




''' 
This function for updata data of specific
by replacing old data by new data 
and saving serializer data then it 
in database
'''
@api_view(['PUT'])
def update_client(request,id):
    data=Client.objects.get(id=id)                       # Client is a model
    serializer=ClientSerializer(data,data=request.data)  #ClientSerializer is a serializer
    if serializer.is_valid:
        serializer.save
        return Response(serializer.data)




'''
this function for deleting the user
'''
@api_view(['DELETE'])
def delete_client(request,id):
    data=Client.objects.get(id=id)                         # Client is a model
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

