from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
	# if get method
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	authentication_classes = [authentication.SessionAuthentication]
	permission_classes = [permissions.DjangoModelPermissions]

	# automaticly called
	# if post method
	def perform_create(self, serializer):
		# serializer.save(user=self.request.user)
		print(serializer.validated_data)
		title = serializer.validated_data.get('title')
		content = serializer.validated_data.get('content') or None
		if content is None:
			content = title

		serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	# lookup_field = 'pk'

# can be set for urls.py lik ethis but extra code
# ProductDetailAPIView = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	lookup_field = 'pk' #make sure we have it

	def perform_update(self, serializer):
		instance = serializer.save()
		if not instance.content:
			instance.content = instance.title
			# doesnt save because already done

class ProductDeleteAPIView(generics.DestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	lookup_field = 'pk' #make sure we have it

	def perform_delete(self, instance):
		super().perform_delete(instance)


class ProductListAPIView(generics.ListAPIView):
	'''
	Not used because instead of prodCreate we can do prodListCreate
	'''
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ProductMixinView(
	mixins.CreateModelMixin,
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	generics.GenericAPIView,
	):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	lookup_field = 'pk'

	# this handle the list view and the detail view
	def get(self, request, *args, **kwargs):
		print(args, kwargs)
		pk = kwargs.get("pk")
		if pk is not None:
			return self.retirieve(request,  *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
	# we will identify the req method
	method = request.method

	if method == "GET":
		# get req -> detail view
		# list view
		if pk is not None:
			obj = get_object_or_404(Product, pk=pk)
			data = ProductSerializer(obj).data
			# detail view
			return Response(data)

		qs = Product.objects.all()
		data = ProductSerializer(qs, many=True).data
		return Response(data)

	if method == "POST":
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			print(serializer.validated_data)
			title = serializer.validated_data.get('title')
			content = serializer.validated_data.get('content') or None
			if content is None:
				content = title
			serializer.save(content=content)
			return Response(serializer.data)
	return Response({"invalid": "not good data"}, status=400 )



