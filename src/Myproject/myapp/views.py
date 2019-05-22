from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from rest_framework import viewsets
from . import models
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

# The Apiview class
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

# The Viewset class

class Helloviewset(viewsets.ViewSet):

    serializer_class = serializers.Helloserializer_two

    def list(self , request):
        list = ['item1' , 'item2' , 'item3' , 'item3']
        return Response({'message' : 'hello_viewset' , 'list' : list})

    def create(self , request):
        serializer = serializers.Helloserializer_two(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            number = serializer.data.get('number')
            message = 'number = {0} , name = {1}'.format(number , name)
            return Response({'message' : message})
        else:
            return Response(serializer.errors ,
             status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self , request , pk = None):
        return Response({'http method' : 'get'})

    def update(self , request , pk = None):
        return Response({'http method' : 'update'})

    def partial_update(self , request , pk = None):
        return Response({'http method' : 'partial update'})

    def destroy(self , request  , pk = None):
        return Response({'http method' : 'destroy'})

# Userprofile Viewset
class Userprofileviewset(viewsets.ModelViewSet):
    serializer_class = serializers.Userprofileserializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.Updateownprofile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
#Login ViewSet
class Loginviewset(viewsets.ViewSet):

    serializer_class = AuthTokenSerializer

    def create(self , request):
        return ObtainAuthToken().post(request)

# Userprofilefeed ViewSet
class Userprofilefeedviewset(viewsets.ModelViewSet):

    permission_classes = (permissions.Postownstatus , IsAuthenticatedOrReadOnly)
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.Profilefeeditemserializer
    queryset = models.Profilefeeditem.objects.all()

    def perform_create(self , serializer):
        serializer.save(user_profile = self.request.user)
