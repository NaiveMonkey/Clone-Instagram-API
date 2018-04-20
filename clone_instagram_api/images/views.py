from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

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
