from django.urls import path
from django.conf.urls import include
from blog import views

urlpatterns = [
    path('posts/', views.PostAPIList.as_view()),
    path('posts/<int:pk>/', views.PostAPIDetail.as_view()),

    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]

