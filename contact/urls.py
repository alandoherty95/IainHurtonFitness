from django.urls import path
from . import views


# Contact app URLs
urlpatterns = [
    path('', views.contact, name='contact'),
]
