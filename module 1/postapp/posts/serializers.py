from matplotlib import category
from posts.models import Post,Category
from rest_framework import serializers
from authentication.serializers import UserSerializer


# CONVERT MODEL ROWS TO JSON
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate(self, validated_data):
        title = validated_data.get('title', None)
        description = validated_data.get('description', None)
        
        if title not in description:
            raise serializers.ValidationError(
                "Description must contains a title")

        return validated_data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True,many=True)

    class Meta:
        model = Post
        fields = "__all__"