from rest_framework.views import APIView
from rest_framework.response import Response


class HellowApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Users HTTP methods as function (get, post, put, patch, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]
        return Response({'message': 'Hellow', 'an_apiview': an_apiview})


