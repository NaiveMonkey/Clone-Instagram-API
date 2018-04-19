from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True) # nested serializer
    likes = LikeSerializer(many=True) # nested serializer

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes'
        )
