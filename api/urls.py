from django.contrib import admin
from django.urls import path, include
from .views import BooksList, BookCreateView, BookDetailsView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("", BooksList.as_view()),
    path("create/", BookCreateView.as_view()),
    path("details/<int:pk>", BookDetailsView.as_view()),
    path("update/<int:pk>", BookUpdateView.as_view()),
    path("delete/<int:pk>", BookDeleteView.as_view()),
    # path("register/", RegisterView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
