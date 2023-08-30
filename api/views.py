from .models import Book, Author, Genre, Publisher
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer, PublisherSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework import filters


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = RegisterSerializer


class BooksList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name', 'genre__name', 'publisher__name']
    ordering_fields = ['id', 'title', 'publisher',
                       'author', 'genre', 'published_date', 'price']

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Book.objects.all()
    #     title = self.request.query_params.get('title')
    #     if title is not None:
    #         queryset = queryset.filter(title=title)
    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author=author)
    #     publisher = self.request.query_params.get('publisher')
    #     if publisher is not None:
    #         queryset = queryset.filter(publisher=publisher)
    #     genre = self.request.query_params.get('genre')
    #     if genre is not None:
    #         queryset = queryset.filter(genre=genre)
    #     return queryset


class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenreCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublisherList(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]


class PublisherCreateView(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]
