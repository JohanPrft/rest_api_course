from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		# you have to name the fields as the one in the class
		fields = [
			'title',
			'content',
			'price',
			'sale_price',
		]
