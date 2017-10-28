from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#index would be the defaulted homepage url thing
def index(request):
	return HttpResponse("inded method")

def helloWorld(request):
	return HttpResponse("new view method")