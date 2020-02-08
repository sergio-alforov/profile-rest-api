from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
