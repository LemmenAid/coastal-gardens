from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
    path('zone-map/', views.zone_map_view, name='zone_map'),
]
