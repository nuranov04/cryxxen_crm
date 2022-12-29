from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model, password_validation

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        # user_activation.delay(user.username, user.email)
        return user

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
