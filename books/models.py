from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='book_reviews')

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
