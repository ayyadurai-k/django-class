from django.http.response import JsonResponse
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


@api_view(["GET"])
def get_hello_world(request):
    print("called")
    data = {
        "message": "Hello , World",
        "quote": "All is well"
    }
    return Response(data)


class PostViewSet(ModelViewSet): 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
