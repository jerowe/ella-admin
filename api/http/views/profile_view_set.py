from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.http.serializers import UserSerializer
from api.http.views.view import BaseViewSet
from api.models import User
from api.permissions import IsSuperuser


class ProfileViewSet(BaseViewSet):
    _request_permissions = {
        'profile': (permissions.IsAuthenticated, IsSuperuser,),
    }

    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['get', 'put'])
    def profile(self, request, *args, **kwargs):
        if request.method == 'PUT':
            serializer = self.get_serializer(request.user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.update(serializer.instance, serializer.initial_data)

            return Response(status=status.HTTP_204_NO_CONTENT)

        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = {
            'method': self.request.method
        }

        return super().get_serializer(*args, **kwargs)