from django.urls import path

from books.views import BookView, ReviewView, ReviewDeleteView

urlpatterns = [
    path('', BookView.as_view(), name='books'),
    path('<int:book_id>/reviews/', ReviewView.as_view(), name='reviews'),
    path('reviews/<int:review_id>/',
         ReviewDeleteView.as_view(), name='delete_review')
]
