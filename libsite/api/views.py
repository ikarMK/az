from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import Book,Author,Publisher
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .serializers import BookSerializer,AuthorSerializer,PublisherSerializer
from django.core.cache import cache
from redis import Redis
from cacheops import cached, cached_view
from rest_framework import status
def counter(func): 
    def wrapper(self, request,*args, **kwargs):
        ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '') 
        counter_ip = 'counter'+ip
        block = 'block:'+ip
        try:
            if(int(cache.get(block))==1):
                return Response({"Dostup": "block"}, status=status.HTTP_404_NOT_FOUND)
        except:
            try:
                count = cache.incr(counter_ip)
            except:
                count = 0
                cache.set(counter_ip,0,timeout=10)
            if(count>5):
                cache.delete(counter_ip)
                cache.set('block',1,timeout=1800)
            return func(self, request,*args, **kwargs)
            
    wrapper.count = 0
    return wrapper

class AuthorView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        author = Author.objects.all().values()
        serializer = AuthorSerializer(author, many=True)
        return Response({"author": serializer.data})

    @counter
    def post(self, request):
        author = request.data.get('author')
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({"success": "Author '{}' created successfully".format(author_saved.name)})
        
    def put(self, request, pk):
        saved_author = get_object_or_404(Author.objects.all(), pk=pk)
        data = request.data.get('author')
        serializer = AuthorSerializer(instance=saved_author, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({
            "success": "Author '{}' updated successfully".format(author_saved.name)
        })

    def delete(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        author.delete()
        return Response({
            "message": "Book with id `{}` has been deleted.".format(pk)
        }, status=204)


class PublisherView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        publisher = Publisher.objects.all().values()
        serializer = PublisherSerializer(publisher, many=True)
        return Response({"publisher": serializer.data})

    @counter
    def post(self, request):
        publisher = request.data.get('publisher')
        serializer = PublisherSerializer(data=publisher)
        if serializer.is_valid(raise_exception=True):
            publisher_saved = serializer.save()
        return Response({"success": "Publisher '{}' created successfully".format(publisher_saved.name)})

    def put(self, request, pk):
        saved_publisher = get_object_or_404(Publisher.objects.all(), pk=pk)
        data = request.data.get('publisher')
        serializer = PublisherSerializer(instance=saved_publisher, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            publisher_saved = serializer.save()
        return Response({
            "success": "Publisher '{}' updated successfully".format(publisher_saved.name)
        })

    def delete(self, request, pk):
        publisher = get_object_or_404(Publisher.objects.all(), pk=pk)
        publisher.delete()
        return Response({
            "message": "Book with id `{}` has been deleted.".format(pk)
        }, status=204)


class BookView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        book = Book.objects.all().values()
        serializer = BookSerializer(book, many=True)
        return Response({"book": serializer.data})

    @counter
    def post(self, request):
        book = request.data.get('book')
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"success": "Book '{}' created successfully".format(book_saved.name)})

    def put(self, request, pk):
        saved_book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data.get('book')
        serializer = BookSerializer(instance=saved_book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({
            "success": "Book '{}' updated successfully".format(book_saved.name)
        })

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        book.delete()
        return Response({
            "message": "Book with id `{}` has been deleted.".format(pk)
        }, status=204)