from rest_framework import serializers

from someapp.models import SomeModel


class SomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = ("title", "created_at", "description")
