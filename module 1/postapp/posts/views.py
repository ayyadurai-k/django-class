from django.http.response import JsonResponse
from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status


# Create your views here.

# C R U D => Create , Read , Update , Delete

# Functions  - API - Application Programming Interface

@api_view(["GET"])  # DECORATOR IT WILL CALL BEFORE FUNCTION CALL AUTOMATICALLY
@permission_classes([IsAuthenticated])
def get_hello_world(request):
    print("user : ", request.user)
    data = {
        "message": "Hello , World",
        "quote": "All is well"
    }
    return Response(data)


# ORM - Object Relational Mapping
@api_view(["GET"])
def get_post(request, id):
    try:
        # SELECT * FROM POST WHERE ID = 1; table row
        post = Post.objects.get(id=id)
        serializer = PostListSerializer(post)  # CONVERT MODEL TO JSON
    except Post.DoesNotExist:
        return Response({"message": "Post doesn't exists , check ID"})
    return Response(serializer.data)


def delete_post(request, id):
    post = Post.objects.get(id=id)  # SELECT * FROM POST WHERE ID = 1;
    post.delete()
    return JsonResponse({"message": f"Post {id} deleted"})


def delete_all_post(request):
    Post.objects.all().delete()
    return JsonResponse({"message": "All posts deleted"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_post(request):
    try:
        user = request.user
        request.data["user"] = user.id
        title = request.data.get("title",None)
        description = request.data.get("description",None)
        
        if not title or not description:
            raise Exception("Please enter value for title and description")
            
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Post created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return  Response({"message" : str(e) },status=400)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def update_post(request, id):
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(
            instance=post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Post updated successfully", "data": serializer.data}, status=200)
    except Post.DoesNotExist:
        return Response({"message": "Post doesn't exists."}, status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def list_posts(request):
    search =  request.query_params.get("search",None)
    print(" search :  ",search)
    if search :
        print(" Called if ")
        posts = Post.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
    else :
        print(" called else ")
        posts = Post.objects.all()
    serializer = PostListSerializer(
        posts, many=True)  # START EXPECTING THE LIST
    return Response(serializer.data,status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_user_posts(request):
    user = request.user
    posts = Post.objects.filter(user=user)
    serializer = PostListSerializer(
        posts, many=True)  # START EXPECTING THE LIST
    return Response(serializer.data,status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_posts(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.filter(user=user)
    serializer = PostListSerializer(
        posts, many=True)  # START EXPECTING THE LIST
    return Response(serializer.data,status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_posts_by_keyword(request, keyword):
    posts = Post.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))
    serializer = PostListSerializer(
        posts, many=True) 
    return Response(serializer.data,status=200)

