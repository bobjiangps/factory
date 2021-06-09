from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
import datetime


class ObtainExpiringAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            if request.path_info.find("/logout/") > 0:
                token.delete()
                return Response({"token": "deleted"})

            # utc_now = datetime.datetime.utcnow().replace(tzinfo=timezone.utc)
            now = datetime.datetime.now()
            if not created:
                if token.created < now - datetime.timedelta(hours=settings.EXPIRE_HOURS):
                    print("re-generate token for old one is expired")
                    token.delete()
                    token = Token.objects.create(user=user)
                    token.created = datetime.datetime.now()
                    token.save()
                else:
                    token.created = datetime.datetime.now()
                    token.save()
            if request.path_info.find("/login/") > 0:
                return Response({"id": user.pk,
                                 "username": user.username,
                                 "mail": user.email,
                                 "token": token.key})
            else:
                return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RevokeAuthToken(APIView):
    queryset = User.objects.none()
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        return Response({"result": "Successfully logged out."}, status=status.HTTP_200_OK)
