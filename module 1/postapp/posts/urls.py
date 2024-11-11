from django.urls import path
from posts.views import get_hello_world,get_hello_world2

urlpatterns = [
    path("get-hello-world/",get_hello_world), # RUN THIS
    path("get-hello-world2/",get_hello_world2),
]
