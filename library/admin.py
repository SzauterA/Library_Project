# Register your models here.
from .models import Book
from django.contrib import admin
from library.filters import PageRangeFilter

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year")
    search_fields = ("title", "author")
    list_filter = ('year', PageRangeFilter)
    ordering = ("title", "author")
    actions_on_top = True
    actions_on_bottom = True
    

admin.site.register(Book, BookAdmin)

