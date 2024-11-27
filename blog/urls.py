from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='home'),
     path('features/', views.PostList.as_view(), name='features'),
     path('<slug:slug>/', views.post_detail, name='post_detail'),
     path('<slug:slug>/edit_comment/<int:comment_id>',
          views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
          views.comment_delete, name='comment_delete'),
     path('<slug:slug>/delete_story/',
          views.delete_story, name='delete_story'),
     #path('test-400/', views.test_400, name='test_400'),
     #path('test-403/', views.test_403, name='test_403'),
     #path('test-404/', views.test_404, name='test_404'),
     #path('test-500/', views.test_500, name='test_500'),
]