from django.http.response import JsonResponse
from posts.models import Post

# Create your views here.

# C R U D => Create , Read , Update , Delete

# Functions  - API - Application Programming Interface


def get_hello_world(request):
    data = {
        "message": "Hello , World",
        "quote": "All is well"
    }
    return JsonResponse(data)


# ORM - Object Relational Mapping

def get_post(request, id):
    try:
        post = Post.objects.get(id=id)  # SELECT * FROM POST WHERE ID = 1;
    except Post.DoesNotExist:
        return JsonResponse({"message": "Post doesn't exists , check ID"})
    data = {
        "id": post.id,
        "title": post.title,
        "description": post.description,
        "image": str(post.image)
    }

    return JsonResponse(data)


def list_posts(request):
    posts = Post.objects.all().values("id", "title", "description", "image") # []
    data = list(posts)
    return JsonResponse(data, safe=False)


def delete_post(request, id):
    post = Post.objects.get(id=id)  # SELECT * FROM POST WHERE ID = 1;
    post.delete()
    return JsonResponse({"message": f"Post {id} deleted"})
