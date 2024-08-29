from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Book, Author
from .forms import BookForm, AuthorForm
from django.utils.translation import gettext as _

# Create your views here.  

def index(request):
    return render(request, "library/index.html")


def books_list(request):
    form = BookForm(request.GET or None)
    books = Book.objects.all()
    no_results = False
    
    if form.is_valid():
        title = form.cleaned_data.get("title")
        if title:
            books = books.filter(title__icontains=title)

        if not books:
            no_results = True
    
    context = {
        "books": books,
        "form": form,
        "no_results": no_results,
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
    if not book.image:
        context['no_image'] = True   
    return render(request, "library/book_details.html", context)


def authors_list(request):
    form = AuthorForm(request.GET or None)
    authors = Author.objects.all()
    no_results = False

    if form.is_valid():
        name = form.cleaned_data.get("name")
        if name:
            authors = authors.filter(name__icontains=name)
        if not authors:
            no_results = True

    return render(request, 'library/authors.html', {
        'form': form,
        'authors': authors,
        'no_results': no_results
    })

def author_details(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        return HttpResponse("Author not found.", status=404)
    try:
        books = Book.objects.filter(author=author)
    except Book.DoesNotExist:
        return HttpResponse("Book not found.", status=404)
    context = {
        "author": author,
        "books": books,
    }
    return render(request, "library/author_details.html", context)


