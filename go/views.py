from django.shortcuts import render
from .models import Author, Book, Engine, Car, Movie, Actor


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'author_list': authors})


def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'author_detail.html', {'author': author})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'book_list': books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'car_list': cars})


def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'car_detail.html', {'car': car})


def engine_list(request):
    engines = Engine.objects.all()
    return render(request, 'engines.html', {'engine_list': engines})


def engine_detail(request, pk):
    engine = Engine.objects.get(pk=pk)
    return render(request, 'engine_detail.html', {'engine': engine})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movie_list': movies})


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})


def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'actors.html', {'actor_list': actors})


def actor_detail(request, pk):
    actor = Actor.objects.get(pk=pk)
    return render(request, 'actor_detail.html', {'actor': actor})
