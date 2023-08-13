from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Author, Genre, Publisher
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        book.save()
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.publisher = validated_data.get('pub', instance.publisher)
        instance.published_date = validated_data.get(
            'pub_date', instance.published_date)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author',
                  'genre', 'publisher', 'published_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class AuthorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    class Meta:
        model = Author
        fields = ['id', 'name', 'age']


class GenreSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    class Meta:
        model = Genre
        fields = ['id', 'name']


class PublisherSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Publisher.objects.create(**validated_data)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address']

#
#    class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )

#     password = serializers.CharField(
#         write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2',
#                   'email', 'first_name', 'last_name')
#         extra_kwargs = {
#             'first_name': {'required': False},
#             'last_name': {'required': False}
#         }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError(
#                 {"password": "Password fields didn't match."})

#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )

#         user.set_password(validated_data['password'])
#         user.save()

#         return user
