from django.contrib import admin
from django.urls import path, include
from .views import BooksList, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("", BooksList.as_view()),
    path("create/", BookCreateView.as_view()),
    path("detail/<int:pk>", BookDetailView.as_view()),
    path("update/<int:pk>", BookUpdateView.as_view()),
    path("delete/<int:pk>", BookDeleteView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
