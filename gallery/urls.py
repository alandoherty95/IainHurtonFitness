from django.urls import path
from . import views


# Gallery app URLs
urlpatterns = [
    path('', views.gallery, name='gallery'),
]
