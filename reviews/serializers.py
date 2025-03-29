from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'movie_title', 'review_content', 'rating', 'user', 'created_date']
        read_only_fields = ['user', 'created_date']

    def validate(self, data):
        if not data.get('movie_title'):
            raise serializers.ValidationError("Movie Title is required.")
        if not data.get('review_content'):
            raise serializers.ValidationError("Review Content is required.")
        return data