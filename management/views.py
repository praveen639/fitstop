from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def foo(requests):
	return HttpResponse('management')