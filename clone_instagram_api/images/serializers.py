from rest_framework import serializers
from . import models

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.Like
        fields = '__all__'
