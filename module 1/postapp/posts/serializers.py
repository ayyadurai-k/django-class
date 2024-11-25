from posts.models import Post
from rest_framework import serializers


# CONVERT MODEL(TABLE) ROWS TO JSON
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
