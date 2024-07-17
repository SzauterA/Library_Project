from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.


def index(request):
    return HttpResponse("Welcome to the library.")


def books_list(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, "library/books.html", context)


def book_details(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return HttpResponse("Book not found.", status=404)
    context = {
        "book": book,
    }
    return render(request, "library/book_details.html", context)