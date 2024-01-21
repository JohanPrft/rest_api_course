from django.db import models

# Create your models here.


class Product(models.Model):
	# Fields are specified by class attributes. You give type and options
	# there an implicit pk
	title = models.CharField(max_length=120)
	content = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

	@property
	def sale_price(self):
		return "%.2f" %(float(self.price) * 0.8)
