from django.contrib import admin
from django.urls import path, include
from django.urls import reverse
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import BookCreateView, BookDetailsView, BooksList, AuthorCreateView, AuthorDetailsView, AuthorList, GenreCreateView, GenreDetailsView, GenreList, PublisherCreateView, PublisherDetailsView, PublisherList
urlpatterns = [
    path("", BooksList.as_view()),
    path("create/", BookCreateView.as_view()),
    path("<int:pk>", BookDetailsView.as_view()),
    # path("update/<int:pk>", BookUpdateView.as_view()),
    # path("delete/<int:pk>", BookDeleteView.as_view()),

    path("author/", AuthorList.as_view()),
    path("author/create/", AuthorCreateView.as_view()),
    path("author/<int:pk>", AuthorDetailsView.as_view()),
    # path("author/update/<int:pk>", AuthorUpdateView.as_view()),
    # path("author/delete/<int:pk>", AuthorDeleteView.as_view()),

    path("genre/", GenreList.as_view()),
    path("genre/create/", GenreCreateView.as_view()),
    path("genre/<int:pk>", GenreDetailsView.as_view()),
    # path("genre/update/<int:pk>", GenreUpdateView.as_view()),
    # path("genre/delete/<int:pk>", GenreDeleteView.as_view()),

    path("publisher/", PublisherList.as_view()),
    path("publisher/create/", PublisherCreateView.as_view()),
    path("publisher/<int:pk>", PublisherDetailsView.as_view()),
    # path("publisher/update/<int:pk>", PublisherUpdateView.as_view()),
    # path("publisher/delete/<int:pk>", PublisherDeleteView.as_view()),

    path("api-auth/", include("rest_framework.urls")),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
