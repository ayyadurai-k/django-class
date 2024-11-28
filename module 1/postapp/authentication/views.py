from django.shortcuts import render
from rest_framework.decorators import api_view
from authentication.serializers import UserSerializer
from rest_framework.response import Response


@api_view(["POST"])
def signup_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "User Created"})
