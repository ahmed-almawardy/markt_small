from user.models import User
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView
    )

from user import serializers


class ConfigUser:
    queryset = User.objects.all()


class Create(ConfigUser, CreateAPIView):
    serializer_class = serializers.UserSerializerCreate
    

class Get(ConfigUser, RetrieveAPIView):
    serializer_class = serializers.UserSerializerRead


class List(ConfigUser, ListAPIView):
    serializer_class = serializers.UserSerializerRead


class Update(ConfigUser, UpdateAPIView):
    serializer_class = serializers.UserPasswordUpdate


class DeleteOne(ConfigUser, DestroyAPIView):
    ...
