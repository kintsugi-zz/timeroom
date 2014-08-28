from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

# Create your views here.
def index(request):
	#request = RequestContext(request)
	return HttpResponse("the beginning of time")