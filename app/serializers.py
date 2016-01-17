from __future__ import unicode_literals

from rest_framework import serializers

from .models import Friend

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'first_name', 'status')