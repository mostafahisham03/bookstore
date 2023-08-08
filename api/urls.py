from django.contrib import admin
from django.urls import path, include
from .views import BooksList, BookView

urlpatterns = [
    path("", BooksList.as_view(), name="book_list"),
    path("create/", BookView.as_view(), name="book_detail"),
]
