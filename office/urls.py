from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^test/$', views.test_celery, name="test_celery"),
    re_path(r'^test2/$', views.test_celery_2, name="test_celery_2")
]
