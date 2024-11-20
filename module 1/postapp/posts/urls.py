from django.urls import path
from posts.views import get_hello_world, get_post, list_posts, delete_post

urlpatterns = [
    path("get-hello-world/", get_hello_world),  # RUN THIS
    path("get/<int:id>/", get_post),  # ONE RECORD
    path("list/", list_posts),  # MULTIPLE RECORDS
    path("delete/<int:id>/", delete_post),  # DELETE ONE RECORD

]
