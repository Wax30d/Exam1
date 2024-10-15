from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Engine(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    horsepower = models.IntegerField()
    fuel_type = models.CharField(max_length=50)

    def __str__(self):
        return f'Fuel HorsePower {self.horsepower}'


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    actors = models.ManyToManyField('Actor')

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
