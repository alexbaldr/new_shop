
from django.urls import path
from main.views import AuthorList, AuthorDetailView, GenreView,\
     PublisherList, BookView, BookDetailView, BookUpdateDestroyView, BookCreateView

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors'),
    path('authors/<slug:slug>/', AuthorDetailView.as_view(),),
    path('genres/', GenreView.as_view(),name='genres'),
    path('publ/', PublisherList.as_view(),name='publ'),
    path('book/', BookView.as_view(),name='book'),
    path('book/update/<int:pk>',  BookUpdateDestroyView.as_view(), name='updes_book'),
    path('book/create', BookCreateView.as_view(), name='create_book'),
    path('book/<int:pk>', BookDetailView.as_view
        ({'get':'list', 'post':'create'})
    ,),

]
