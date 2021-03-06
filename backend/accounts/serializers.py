from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = [
            "url",
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]
