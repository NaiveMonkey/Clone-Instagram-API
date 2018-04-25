from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status

# Create your views here.
class Notifications(APIView):

    def get(self, request, format=None):

        user = request.user

        notification = models.Notification.objects.filter(to=user)

        serializer = serializers.NotificationSerializer(notification, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

def create_notification(creator, to, type, image = None, comment = None):

    notification = models.Notification.objects.create(
        creator=creator,
        to=to,
        notification_type=type,
        image=image,
        comment=comment
    )

    notification.save()
