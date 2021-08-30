from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class PostSerializer(serializers.ModelSerializer):
    autor = UserSerializer()
    # nome_autor = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'