from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly, IsAdminUser)
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Authors, Books, Comments, Genres, Publishers
from main.my_Generic_API import UpdateDestroyAPIView
from main.serializers import (AuthorSerializer, BookDetailSerializer,
                              BookSerializer, CommentCreateSerializer,
                              CommentSerializer, GenreSerializer,
                              PublisherSerializer, AuthorsDetailSerializer)
from django.contrib.auth import get_user_model
from main.mixins import LikedMixin

class AuthorList(generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def get(self, request, slug):
        queryset = get_object_or_404(Authors, slug=slug)
        serializer = AuthorsDetailSerializer(queryset)
        return Response(serializer.data)
    
    def post(self, request, slug):
        serializer = AuthorsDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors)    


class PublisherList(APIView):
    permission_classes = (IsAdminUser,)
    def post(self, request, *args, **kwargs):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, *args, **kwargs):
        queryset = Publishers.objects.all()
        serializer = PublisherSerializer(queryset, many=True)
        return Response(serializer.data)


class GenreView(APIView):
    permission_classes = (IsAdminUser,)
    def post(self, request, *args, **kwargs):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, *args, **kwargs):
        queryset = Genres.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)


class BookView(generics.ListAPIView):
    # permission_classes = (AllowAny)
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends= (DjangoFilterBackend,)
    filterset_fields=('author', 'genre',)

class BookDetailView(viewsets.ViewSet, LikedMixin):
    # permission_classes = (AllowAny)
    def list(self, request, pk=None):
        queryset = Books.objects.all()
        obj = get_object_or_404(queryset, pk=pk)
        serializer = BookDetailSerializer(obj)
        return Response(serializer.data)
    
    def create(self, request, pk=None, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = CommentSerializer(data = 
                                        {'book': pk,
                                        'user': request.user.id, 
                                        'text': request.data['text']})

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,
                            status=status.HTTP_201_CREATED,
                            )
            return Response(serializer.errors)
        else:
            return Response('HTTP 401 Unauthorized')

    def destroy(self, request, pk=None, *args, **kwargs):
        if request.user.is_authenticated:
            pass

class BookUpdateDestroyView(UpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]