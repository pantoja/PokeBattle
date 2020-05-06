from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.get_short_name()

    class Meta:
        model = User
        fields = ["id", "email", "name"]
