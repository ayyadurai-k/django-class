from django.urls import path
from posts.views import get_hello_world, get_post, list_posts, delete_post, delete_all_post, create_post, update_post,list_user_posts,get_user_posts

urlpatterns = [
    path("get-hello-world/", get_hello_world),  # RUN THIS
    path("get/<int:id>/", get_post),  # ONE RECORD
    path("get-user/<int:user_id>/", get_user_posts),
    path("list/", list_posts),  # MULTIPLE RECORDS
    path("user-list/", list_user_posts),  # MULTIPLE RECORDS
    path("delete/<int:id>/", delete_post),  # DELETE ONE RECORD
    path("delete-all/", delete_all_post),  # DELETE ALL RECORD
    path("create/", create_post),  # CREATE ONE RECORD
    path("update/<int:id>/", update_post),  # UPDATE ONE RECORD
]
