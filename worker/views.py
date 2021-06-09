from django.shortcuts import HttpResponse


def debug(request):
    return HttpResponse("debug")
