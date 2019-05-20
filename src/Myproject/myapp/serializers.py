from rest_framework import serializers

#serializer for Helloapiview
class Helloserializer(serializers.Serializer):

    name = serializers.CharField(max_length = 10)

#serializer for Helloviewset
class Helloserializer_two(serializers.Serializer):
    name = serializers.CharField(max_length = 10)
    number = serializers.IntegerField()
