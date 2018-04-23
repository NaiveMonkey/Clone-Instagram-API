from rest_framework import serializers
from . import models
from clone_instagram_api.users import models as user_models

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields =(
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True) # nested serializer
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'creator'
        )
