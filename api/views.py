from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BooksList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():  # -----1 & 2
            serializer.save()  # -----3
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):
    def get(self, request, **kwargs):
        book = Book.objects.get(id=kwargs['pk'])
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)

    def put(self, request, **kwargs):
        book = Book.objects.get(id=kwargs['pk'])
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        book = Book.objects.get(id=kwargs['pk'])
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
