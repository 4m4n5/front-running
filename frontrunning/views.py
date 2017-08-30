from django.shortcuts import render
# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages	
from django.http import HttpResponseRedirect

from frontrunning.models import *

import json

def add_fraud(trade_list):
	FraudList.objects.create(
		party_1 = trade_list[0].trade_id,
		party_2 = trade_list[1].trade_id,
		party_3 = trade_list[2].trade_id, 
		security = trade_list[0].security_name
	)

def get_data_fraud(list, security_name):
	result = []
	for fraud in list:
		temp_list = []
		if (fraud.security == 'apple'):
			party_1 = AppleOrder.objects.get(trade_id=fraud.party_1)
			party_2 = AppleOrder.objects.get(trade_id=fraud.party_2)
			party_3 = AppleOrder.objects.get(trade_id=fraud.party_3)
		if (fraud.security == 'walmart'):
			party_1 = WalmartOrder.objects.get(trade_id=fraud.party_1)
			party_2 = WalmartOrder.objects.get(trade_id=fraud.party_2)
			party_3 = WalmartOrder.objects.get(trade_id=fraud.party_3)
		if (fraud.security == 'facebook'):
			party_1 = FacebookOrder.objects.get(trade_id=fraud.party_1)
			party_2 = FacebookOrder.objects.get(trade_id=fraud.party_2)
			party_3 = FacebookOrder.objects.get(trade_id=fraud.party_3)
		temp_list.append(party_1)
		temp_list.append(party_2)
		temp_list.append(party_3)
		result.append(temp_list)
		result.reverse()
		for arr in result:
			arr.reverse()
	return result

def render_fraud(security_name):
	list = FraudList.objects.all()
	fraud_data = get_data_fraud(list, security_name)
	return fraud_data
	


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
			# trade_id = trade_id,
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
			# trade_id = trade_id,
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
			# trade_id = trade_id,
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
		fraudlist.reverse()
		main = fraudlist.pop(0)
		counter = 0
		commit_list = []
		commit_list.append(main)
		for fraud in fraudlist:
			commit_list.append(fraud)
			counter = counter + 1
			if counter == 2:
				add_fraud(commit_list)
				commit_list = []
				commit_list.append(main)
				counter = 0
		fraud_data = render_fraud(security_name)
		return render(request, 'fraud.html', {'fraud_data': fraud_data})
	else:
		messages.add_message(request, messages.INFO, 'Trade added Successfully. No front running detected.')
		return render(request, 'index.html')

	