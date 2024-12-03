from django.shortcuts import render
from rest_framework.decorators import api_view
from authentication.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(["POST"])
def signup_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "User Created"})


@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=400)

    user = authenticate(username=username, password=password)

    if not user:
        return Response({"error": "Invalid credentials"}, status=401)

    token = Token.objects.create(user=user)

    return Response({"message": "Login successful", "key": token.key})


def list_user(request):
    pass


def get_user(request, id):
    pass
