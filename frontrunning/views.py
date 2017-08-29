from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse

from frontrunning.models import *

import json

def index(request):
	return render_to_response('index.html')