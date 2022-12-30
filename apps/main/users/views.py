from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins

from .serializers import UserSerializer, UserShortInfoSerializer, UserDetailSerializer, ChangeUserPasswordSerializer

User = get_user_model()


class UserApiViewSet(ModelViewSet):
    queryset = User.objects.select_related("status").all()
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

# class UserInfo(GenericViewSet,
#                mixins.ListModelMixin):
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer
#     permission_classes = [IsAuthenticated]
#
#     def list(self, request, *args, **kwargs):
#         queryset = User.objects.select_related("status").get(id=request.user.id)
#         return Response(UserDetailSerializer(queryset).data)
