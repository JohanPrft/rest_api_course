from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from products.models import Product


# API based view, send a json response back
def api_home(request):
	# JsonResponse takes a dict object
	return JsonResponse({"message": "Hi there its API"})


# get the data in the request
def echo(request):
	body = request.body  # byte string of JSON data
	data = {}
	try:
		data = json.loads(body)
	except:
		pass
	print(data)
	return JsonResponse({"message": "Hi there its API"})


def random_object(request):
	# return a random obj
	# Product.objects.all():  all instances of the Product model from the database.
	model_data = Product.objects.all().order_by("?").first()
	data = {}
	if model_data:
		data['id'] = model_data.id # by default in a model
		data['title'] = model_data.title
		data['content'] = model_data.content
		data['price'] = model_data.price
		# ... tedious
		# basic serialization
	return JsonResponse(data)
