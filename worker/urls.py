from django.urls import path
from . import views


urlpatterns = [
    path(r'debug/', views.debug, name="debug"),
]
