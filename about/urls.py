from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
    path('get-started/', views.get_started_view, name='get_started'),
    path('zone-map/', views.zone_map_view, name='zone_map'),
]