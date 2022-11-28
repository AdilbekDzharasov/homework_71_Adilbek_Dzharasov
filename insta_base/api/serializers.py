from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'author', 'likes')
        read_only_fields = ('id',)

