from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.PostList.as_view(), name='features'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
