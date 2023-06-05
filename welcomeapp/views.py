from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=pink><h1><centre>welcome to aswithait</centre></h1><body><html>""")
    return res
