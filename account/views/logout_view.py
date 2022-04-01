from django.contrib.auth import logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


class Logout(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            print('inja')
            refresh_token = request.data["refresh"]
            print(refresh_token)
            print('here')
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            data = {'Response': 'successful'}
            p_status = status.HTTP_205_RESET_CONTENT
        except Exception as e:
            data = {'Response': 'could not find user'}
            p_status = status.HTTP_400_BAD_REQUEST
        finally:
            return Response(data=data, status=p_status)
