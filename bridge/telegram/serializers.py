from rest_framework import serializers
from django.db import models
from telegram.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ("channel_id", "name")
