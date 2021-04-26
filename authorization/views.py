# from rest_framework_jwt.utils import jwt_payload_handler
from new_shop import settings
from rest_framework import request, status, generics
from rest_framework.authentication import (BaseAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from .license import IsOwnerProfileOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from authorization.models import User
from authorization.serializers import UserSerializer
from  authorization.tasks import mail_for_new_user


class CreateUserView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=serializer.data.get('email'))
        print('this is',user.id, user.email)
        mail_for_new_user(get_user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# class GetUserView(APIView):
#     permission_classes = (IsAuthenticated)

#     def get(self, request):
#         queryset = User.objects.get(id=request.user.id)
#         serializer = UserSerializer(queryset)
#         return Response(serializer.data)

class GetUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
