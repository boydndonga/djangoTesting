from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home_page(self):
    return HttpResponse('<html><title>my home page</title></html>')
