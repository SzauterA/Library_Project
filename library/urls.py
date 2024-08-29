from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.books_list, name="books_list"),
    path("books/<int:book_id>", views.book_details, name="book_details"),
    path("authors/", views.authors_list, name="authors_list"),
    path("authors/<int:author_id>/", views.author_details, name="author_details"),
]
