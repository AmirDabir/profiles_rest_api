from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
# Create your views here.

class Helloapiview(APIView):

    serializer_class = serializers.Helloserializer

    def get(self , request , format = None):
        list = ['item1' , 'item2' , 'item3' , 'item4']
        return Response({'Message' : "Hello" , 'list' : list})


    def post(self , request):

        serializer = serializers.Helloserializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


    def put(self , request , pk = None):
        return Response({'method' : 'put'})

    def patch(self , request , pk = None):
        return Response({'method' : 'patch'})

    def delete(self , request , pk = None):
        return Response({'method' : 'delete'})
