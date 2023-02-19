from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from books.models import Book, Review
from books.serializers import BookSerializer, ReviewSerializer


class BookView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class ReviewView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, book_id):
        data = request.data.copy()
        data['book'] = book_id
        data['user'] = request.user.id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, book_id):
        reviews = Review.objects.filter(book_id=book_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)

            if request.user == review.user:
                review.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)

        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
