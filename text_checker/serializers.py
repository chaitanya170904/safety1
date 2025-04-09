from rest_framework import serializers

class TweetSerialzer(serializers.Serializer):
    text=serializers.CharField(max_length=280)