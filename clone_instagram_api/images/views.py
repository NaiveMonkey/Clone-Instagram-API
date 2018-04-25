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

            # 모든 image 중에서 2개만 가져올 것
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

            return Response(status=status.HTTP_304_NOT_MODIFIED)
        except models.Like.DoesNotExist:

            models.Like.objects.create(
                creator=user,
                image = found_image
            )

            return Response(status=status.HTTP_200_OK)

class UnLikeImage(APIView):

    def delete(self, request, image_id, format=None):

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

            return Response(status=status.HTTP_304_NOT_MODIFIED)


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

class Comment(APIView):

    def delete(self, request, comment_id, formant=None):

        user = request.user

        try:
            # comment 의 creator 와 삭제하고자 명령하는 user 가 서로 같아야함
            comment = models.Comment.objects.get(id=comment_id, creator=user)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class Search(APIView):

    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags', None)

        if hashtags is not None:

            hashtags = hashtags.split(",")

            images = models.Image.objects.filter(tags__name__in=hashtags).distinct()

            serializer = serializers.CountImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
