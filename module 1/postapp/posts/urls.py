from django.urls import path
from posts.views import get_hello_world, get_post

urlpatterns = [
    path("get-hello-world/", get_hello_world),  # RUN THIS
    path("get/", get_post),
]
