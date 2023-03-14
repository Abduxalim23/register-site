from django.urls import path
from .views import post_register
urlpatterns = [
    path('reg/', post_register, name='post-register'),
]
