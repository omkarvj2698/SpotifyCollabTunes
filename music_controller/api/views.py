from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse


# Create your views here.
def main(request):
    return HttpResponse("Hello")

