from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register('produduct-abc', ProductViewSet,
				basename='products')
