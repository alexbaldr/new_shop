from rest_framework.decorators import action
from rest_framework.response import Response

from main import serv
from authorization.serializers import UserSerializer


class LikedMixin:

    @action(detail=True)
    def like(self, request,pk=None):
        obj = self.get_object()
        serv.add_like(obj, request.user)
        return Response()
    
    @action(detail=True)
    def unlike(self, request,pk=None):
        obj = self.get_object()
        serv.remove_like(obj, request.user)
        return Response()

    @action(detail=True)
    def fans(self, request, pk=None):
        obj = self.get_object()
        fans = serv.get_fans(obj)
        serializer = UserSerializer(fans, many=True)
        return Response(serializer.data)
