from rest_framework import serializers
from books.models import Book, Review
from django.contrib.auth import get_user_model

User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'owner']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'rating', 'review_text', 'created_at', 'book', 'user']
        read_only_fields = ['id', 'created_at', 'user', 'book']
