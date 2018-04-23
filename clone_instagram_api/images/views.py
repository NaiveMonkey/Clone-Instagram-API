from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status

# Create your views here.
class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        images_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:

                images_list.append(image)

        sorted_list = sorted(images_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImagesSerializer(sorted_list, many=True)

        return Response(serializer.data)

class LikeImage(APIView):

    def post(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisiting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            preexisiting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Like.DoesNotExist:

            models.Like.objects.create(
                creator=user,
                image = found_image
            )

            return Response(status=status.HTTP_200_OK)

class CommentOnImage(APIView):

    def post(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(creator=user, image=found_image)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(data=serializer.errors, status= status.HTTP_405_METHOD_NOT_ALLOWED)
