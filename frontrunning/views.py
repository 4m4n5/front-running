from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse

from frontrunning.models import *

import json

def index(request):
	return render_to_response('index.html')

def add_trade(request):
	trade_id = request.GET.get('tradeid')
	customer_id = request.GET.get('customerid')
	trade_type = request.GET.get('tradetype')
	security_name = request.GET.get('securityname')
	security_type = request.GET.get('securitytype')
	quantity = request.GET.get('quantity')
	price = request.GET.get('price')
	if (security_name == 'facebook'):
		trade_instance = FacebookOrder.objects.create(
			trade_id = trade_id,
			customer_id = customer_id,
			trade_type = trade_type,
			security_type = security_type,
			security_name = security_name,
			price = price,
			quantity = quantity
		)
		items = FacebookOrder.objects.filter().order_by('-trade_id')[:30]

	if (security_name == 'apple'):
		trade_instance = AppleOrder.objects.create(
			trade_id = trade_id,
			customer_id = customer_id,
			trade_type = trade_type,
			security_type = security_type,
			security_name = security_name,
			price = price,
			quantity = quantity
		)
		items = AppleOrder.objects.filter().order_by('-trade_id')[:30]

	if (security_name == 'walmart'):
		trade_instance = WalmartOrder.objects.create(
			trade_id = trade_id,
			customer_id = customer_id,
			trade_type = trade_type,
			security_type = security_type,
			security_name = security_name,
			price = price,
			quantity = quantity
		)
		items = WalmartOrder.objects.filter().order_by('-trade_id')[:30]

	X = items[0]
	alert = False
	fraudlist = []
	if (X.security_type != 'put_option'):
		for trade in items:
			if(trade.customer_id != X.customer_id and trade.customer_id != 1 and ((trade.trade_type != X.trade_type and trade.security_type != "put_option") or (trade.trade_type == X.trade_type and trade.security_type == 'put_option'))):
				alert = True
				Z = trade
			if(trade.customer_id == X.customer_id and trade.trade_type != X.trade_type and alert == True and trade.security_type == X.security_type):
				fraudlist.append(trade)
				fraudlist.append(Z)
				fraudlist.append(X)
				alert = False
				break

	if (X.security_type == "put_option"):
		for trade in items:
			if(trade.customer_id != X.customer_id and trade.customer_id != 1 and (( trade.trade_type != X.trade_type and trade.security_type == X.security_type) or (trade.trade_type == X.trade_type and trade.security_type != X.security_type))):
				alert = True
				Z = trade 

			if(trade.customer_id == X.customer_id and trade.trade_type != X.trade_type and alert == True and trade.security_type == X.security_type):
				fraudlist.append(trade)
				fraudlist.append(Z)
				fraudlist.append(X)
				alert = False
				break

	if fraudlist:
		response_data = {'a': fraudlist[0],
						'b' : fraudlist[1],
						'c' : fraudlist[2]
						}

	else:
		response_data = {'message' : 'no front running'}


	return JsonResponse(response_data)