from django.urls import path
from authorization.views import CreateUserView, GetUserView

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('profile/<int:pk>/', GetUserView.as_view(),name="profile"),
]