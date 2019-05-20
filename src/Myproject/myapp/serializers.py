from rest_framework import serializers
from . import models
#serializer for Helloapiview
class Helloserializer(serializers.Serializer):

    name = serializers.CharField(max_length = 10)

#serializer for Helloviewset
class Helloserializer_two(serializers.Serializer):
    name = serializers.CharField(max_length = 10)
    number = serializers.IntegerField()

# Model serializer
class Userprofileserializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id' , 'name' , 'email' , 'password')
        extra_kwargs = {'password' : {'write_only' : True}}
    def create(self , validated_data):
        user = models.UserProfile(
        email = validated_data['email'],
        name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
