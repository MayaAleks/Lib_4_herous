from django.contrib import admin

# Register your models here.
from main.models import Books, Author, Genre, Customers, ImageAuthor, ImageBook, BookInstance

admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Customers)
admin.site.register(ImageAuthor)
admin.site.register(ImageBook)
admin.site.register(BookInstance)
