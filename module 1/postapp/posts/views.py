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

def get_post(request):
    post = Post.objects.get(id=id)  # SELECT * FROM POST WHERE ID = 1;
    data = {
        "id": post.id,
        "title": post.title,
        "description": post.description,
        "image": str(post.image)
    }

    return JsonResponse(data)
