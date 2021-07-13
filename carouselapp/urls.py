from django.urls import path
from .import views

app_name = 'carouselapp'

urlpatterns = [
    path('', views.carosel, name='carosel')
]