from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Password not returned in responses

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Hash password on creation
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))  # Hash new password on update
        return super().update(instance, validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Show user details, but read-only

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