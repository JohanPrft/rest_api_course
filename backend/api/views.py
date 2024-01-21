from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

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
	# ... tedious (can use model_to_dict)
	# basic serialization
	return JsonResponse(data)

@api_view(["GET"])
def random_object_rest(request):
	model_data = Product.objects.all().order_by("?").first()
	data = {}
	if model_data:
		model_to_dict(model_data)
	return Response(data)


@api_view(["GET"])
def random_object_rest_serialize(request):
	instance = Product.objects.all().order_by("?").first()
	data = {}
	if instance:
		data = ProductSerializer(instance).data
	return Response(data)


@api_view(["POST"])
def post_req(request):
	serializer = ProductSerializer(data=request.data)
	if serializer.is_valid():
		instance = serializer.save()
		print(instance)
		return JsonResponse(serializer.data)
	return Response({"invalid": "not good data"}, status=400 )
