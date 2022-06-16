from django.db import models

class Author(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    surname = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthday = models.DateField()

class Publisher(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    name = models.CharField(max_length=255)

class Book(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    name = models.CharField(max_length=255)
    number_page = models.IntegerField(primary_key=False)
    publication_date = models.DateField()
    author = models.ForeignKey(Author,related_name='author_id', on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='publisher_id', on_delete=models.CASCADE)
