
from rest_framework import serializers


class JsonFileInputSerializer(serializers.Serializer):
    json_file = serializers.FileField(required=True)
