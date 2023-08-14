from django.contrib import admin
from django.urls import path, include
from .views import BooksList, BookCreateView, BookDetailsView, BookUpdateView, BookDeleteView, AuthorList,  AuthorCreateView, AuthorDetailsView, AuthorUpdateView, AuthorDeleteView, GenreList, GenreCreateView, GenreDetailsView, GenreUpdateView, GenreDeleteView, PublisherList, PublisherCreateView, PublisherDetailsView, PublisherUpdateView, PublisherDeleteView

urlpatterns = [
    path("", BooksList.as_view()),
    path("create/", BookCreateView.as_view()),
    path("<int:pk>", BookDetailsView.as_view()),
    path("update/<int:pk>", BookUpdateView.as_view()),
    path("delete/<int:pk>", BookDeleteView.as_view()),

    path("author/", AuthorList.as_view()),
    path("author/create/", AuthorCreateView.as_view()),
    path("author/<int:pk>", AuthorDetailsView.as_view()),
    path("author/update/<int:pk>", AuthorUpdateView.as_view()),
    path("author/delete/<int:pk>", AuthorDeleteView.as_view()),

    path("genre/", GenreList.as_view()),
    path("genre/create/", GenreCreateView.as_view()),
    path("genre/<int:pk>", GenreDetailsView.as_view()),
    path("genre/update/<int:pk>", GenreUpdateView.as_view()),
    path("genre/delete/<int:pk>", GenreDeleteView.as_view()),

    path("publisher/", PublisherList.as_view()),
    path("publisher/create/", PublisherCreateView.as_view()),
    path("publisher/<int:pk>", PublisherDetailsView.as_view()),
    path("publisher/update/<int:pk>", PublisherUpdateView.as_view()),
    path("publisher/delete/<int:pk>", PublisherDeleteView.as_view()),

    path("api-auth/", include("rest_framework.urls")),
]
