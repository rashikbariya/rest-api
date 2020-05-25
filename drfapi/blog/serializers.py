from rest_framework import serializers
from .models import Posts

# from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Posts
        fields = ['id', 'content','image','owner']


# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Posts.objects.all())
    
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'posts']