from django.shortcuts import render, HttpResponse
from .tasks import add


def test_celery(request):
    add.delay(3, 5)
    return HttpResponse("Celery works")

def test_celery_2(request):
    result = add.apply_async(args=[4, 7])
    print(request)
    return HttpResponse(result.task_id + ' : ' + result.status)
