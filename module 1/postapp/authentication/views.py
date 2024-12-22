from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from authentication.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def signup_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "User Created"})


@api_view(["POST"])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
    token = AccessToken.for_user(user)
    response = Response({'message': 'Logged in successfully'},status=200)
    
    # Set JWT as HttpOnly cookie
    response.set_cookie(
        key='jwt',
        value=str(token),
        httponly=True,
        samesite='Strict', # Optional: To prevent CSRF
        max_age=365 * 24 * 60 * 60, # 1 year
    )
    return response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    response = Response({'message': 'Logged out successfully'},
    status=200)
    # Clear the cookie
    response.delete_cookie('jwt')
    return response

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
