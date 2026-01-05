from django.urls import path
from . import views

app_name = 'ninetynine_days_in_the_forest'

urlpatterns = [
    path('', views.home, name='home'),
    path('days/', views.days, name='days'),
    path('day/<int:day>/', views.day_detail, name='day_detail'),
    path('about/', views.about, name='about'),
]
