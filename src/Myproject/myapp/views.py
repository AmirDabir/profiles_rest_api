from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):

    def get(self , request , format = None):
        an_apiview = [
            'content 1',
            'content 2',
            'content 3'
        ]
        return Response({'message':'Hello' , 'an_api view' : an_apiview})
