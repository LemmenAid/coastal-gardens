from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
    path('get-started/', views.get_started_view, name='get_started'),
    path('zone-map/', views.zone_map_view, name='zone_map'),
]