from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation

from apps.main.roles.serializers import RoleSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "status",
            "email",
            "first_name",
            "last_name",
            "rating",
            "password",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        # user_activation.delay(user.username, user.email)
        return user

    def validateStreamHandler_password(self, value):
        password_validation.validate_password(value)
        return value


class UserDetailSerializer(serializers.ModelSerializer):
    status = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "status",
            "last_login",
            "created_at",
            "email",
            "first_name",
            "last_name",
            "rating",
            # "groups",
        )


class UserShortInfoSerializer(serializers.ModelSerializer):
    status = RoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "status",
            "email",
            "first_name",
            "last_name",
            "rating",
        )


class ChangeUserPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)
