from rest_framework import serializers
from main.models import (Authors, Comments, Books, Publishers, Genres, Like)

class AuthorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        exclude = ['slug']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        exclude = ['slug', 'bio']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = '__all__'
 
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'
       
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ['name', 'author']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['user','text', 'date', 'total_likes']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like


class BookDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, source='comments_book')
    author = AuthorSerializer(many=True, read_only=True)
    class Meta:
        model = Books
        fields = ['name', 'author', 'genre', 'publisher','total_likes', 'comments']
