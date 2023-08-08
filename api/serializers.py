from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        book.save()
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.pub = validated_data.get('pub', instance.pub)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ['title', 'price', 'author', 'genre', 'pub', 'pub_date']
