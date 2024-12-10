from posts.models import Post
from rest_framework import serializers
from authentication.serializers import UserSerializer


# CONVERT MODEL ROWS TO JSON
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
