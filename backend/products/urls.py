from django.urls import path

from . import views

# /api/products/
urlpatterns = [
	path('', views.ProductListCreateAPIView.as_view()),
	# int then lookup field as key arg
	path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
	path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
	path('<int:pk>/', views.ProductDetailAPIView.as_view()),
]
