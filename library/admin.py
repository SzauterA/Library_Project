from django.contrib import admin
from .models import Book, Author
from library.filters import PageRangeFilter

class BookAdmin(admin.ModelAdmin):
    def get_authors(self, obj):
        return ", ".join(author.name for author in obj.author.all())
    get_authors.short_description = 'Authors'

    list_display = ("title", "get_authors", "year")
    search_fields = ("title", "author__name")  
    list_filter = ('year', PageRangeFilter)
    ordering = ("title",)
    actions_on_top = True
    actions_on_bottom = True

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)
    actions_on_top = True
    actions_on_bottom = True

admin.site.register(Author, AuthorAdmin)




