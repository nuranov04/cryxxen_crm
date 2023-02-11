from django.contrib.auth import get_user_model
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from apps.internship.groups.models import Bunch
from apps.internship.groups.serializers import BunchShortInfoSerializer
from utils import permissions
from apps.main.users.serializers import (
    UserSerializer,
    UserShortInfoSerializer,
    UserDetailSerializer,
    ChangeUserPasswordSerializer
)

User = get_user_model()


class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        if self.action == "list":
            return UserShortInfoSerializer
        return UserSerializer

    @action(
        detail=False, permission_classes=[IsAuthenticated], methods=["get"]
    )
    def get_userinfo(self, request, email=None):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Change Password of User",
        method="post",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "old_password": openapi.Schema(type=openapi.TYPE_STRING),
                "new_password": openapi.Schema(type=openapi.TYPE_STRING),
                "confirm_new_password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: openapi.Response(
                "Change Password of User",
                ChangeUserPasswordSerializer(),
            )
        },
    )
    @action(
        detail=True, permission_classes=[IsAuthenticated], methods=["post"]
    )
    def change_password(self, request, email=None):
        user = self.get_object()
        serializer = ChangeUserPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_password = serializer.data.get("old_password")
        new_password = serializer.data.get("new_password")
        confirm_new_password = serializer.data.get("confirm_new_password")
        if not user.check_password(old_password):
            return Response(
                {"old_password": ["Wrong current password."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if new_password == confirm_new_password:
            user.set_password(new_password)
            user.save()
            return Response(
                {"detail": "Password updated successfully"}, status=status.HTTP_200_OK
            )
        return Response(
            {"detail": "Not correct password"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        methods=["GET"], detail=False, url_path="intern_groups", permission_classes=[permissions.IsIntern]
    )
    def intern_groups(self, request, email=None):
        queryset = Bunch.objects.prefetch_related("members", "mentors").filter(members=request.user).last()
        serializer = BunchShortInfoSerializer(queryset)
        return Response(
            data=serializer.data,
            status="200"
        )

    @action(
        methods=["GET"], detail=False, url_path="mentor_groups", permission_classes=[permissions.IsMentor]
    )
    def mentor_groups(self, request, email=None):
        queryset = Bunch.objects.filter(mentors=request.user).all()
        serializer = BunchShortInfoSerializer(queryset, many=True)
        return Response(
            data=serializer.data,
            status="200"
        )
