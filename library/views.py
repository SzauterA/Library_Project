from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.  

def index(request):
    return render(request, "library/index.html")

def books_list(request):
    form = BookForm(request.GET or None)
    books = Book.objects.all()
    no_results = False
    
    if form.is_valid():
        title = form.cleaned_data.get("title")
        author = form.cleaned_data.get("author")
        books = Book.objects.filter(title__icontains=title, author__icontains=author)
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