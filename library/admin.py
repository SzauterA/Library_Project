from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year")
    search_fields = ("title", "author")
    list_filter = ("year",)
    ordering = ("author", "title", "year")

admin.site.register(Book, BookAdmin)

