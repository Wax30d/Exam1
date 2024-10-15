from django.contrib import admin
from .models import Book, Author, Car, Engine, Movie, Actor
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Car)
admin.site.register(Engine)
admin.site.register(Movie)
admin.site.register(Actor)
