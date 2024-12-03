from django.http.response import JsonResponse
from posts.models import Post
from posts.serializers import PostSerializer
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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
        serializer = PostSerializer(post)  # CONVERT MODEL TO JSON
    except Post.DoesNotExist:
        return Response({"message": "Post doesn't exists , check ID"})
    return Response(serializer.data)


@api_view(["GET"])
def list_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)  # START EXPECTING THE LIST
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
    user = request.user
    request.data["user"] = user.id

    print(" request.data : ", request.data)

    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "Post created successfully", "data": serializer.data}, status=201)


def update_post(request, id):
    try:
        post = Post.objects.get(id=id)  # SELECT * FROM POST WHERE ID = 1
        data = json.loads(request.body)  # JSON TO DICTIONARY

        title = data.get("title")
        description = data.get("description")

        post.title = title
        post.description = description

        post.save()

    except Post.DoesNotExist:
        return JsonResponse({"message": "Post doesn't exists , check ID"})

    return JsonResponse({"message": f"Post {post.id} updated"})
