from rest_framework import serializers
from users.models import GigAccount


class GigAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = GigAccount
        fields = "__all__"
