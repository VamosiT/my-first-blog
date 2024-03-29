from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name="post_new"),
    path('post/<int:pk>/edit/', views.post_edit, name="post_edit"),
    path('static_about', views.static_about, name="static_about"),
    path('signup', views.signup_view, name="signup"),
    path('gamf', views.gamf, name="gamf"),


]
