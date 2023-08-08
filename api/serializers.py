from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book
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
        instance.pub = validated_data.get('pub', instance.pub)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author', 'genre', 'pub', 'pub_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


# class RegisterSerializer(serializers.ModelSerializer):
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
