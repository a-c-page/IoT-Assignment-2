from django.urls import path
from .views import state

urlpatterns = [
    path('state/', state)
]