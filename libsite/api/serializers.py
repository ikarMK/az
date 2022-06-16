from dataclasses import fields
from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from pkg_resources import require
from rest_framework import serializers
from .models import Book, Author,Publisher

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    surname = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(max_length=255)
    birthday = serializers.DateField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.save()
        return instance
        
class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    def create(self, validated_data):
        return Publisher.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    number_page = serializers.IntegerField()
    publication_date = serializers.DateField()
    author_id = serializers.SerializerMethodField()
    publisher_id = serializers.SerializerMethodField()

    def get_author_id(self, obj):
        return Author.objects.filter(id=obj.get('author_id')).values('id','name','surname','middle_name','birthday')[0]
    def get_publisher_id(self, obj):
        return Publisher.objects.filter(id=obj.get('author_id')).values('id','name')[0]
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number_page = validated_data.get('number_page', instance.number_page)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.publisher_id = validated_data.get('publisher_id', instance.publisher_id)
        instance.save()
        return instance
