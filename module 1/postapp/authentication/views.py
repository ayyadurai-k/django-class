from django.shortcuts import render
from rest_framework.decorators import api_view
from authentication.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


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

@api_view(["GET"])
def get_user(request, id):
    try:
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response({"message": "User fetched successfully", "data": serializer.data},status=200)
    except User.DoesNotExist:
        return Response({"message": "User Doesn't Exists"},status=404)
