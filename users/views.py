from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from users.serializers import UserSerializer

User = get_user_model()


@method_decorator(csrf_exempt, name='dispatch')
class UserRegister(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data.get("username"))
            token = RefreshToken.for_user(user)
            ret = {
                "username": user.username,
                "refresh": str(token),
                "access": str(token.access_token)
            }
            return Response(data=ret, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
