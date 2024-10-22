from django.urls import path
from .views.products import ProductApiView

urlpatterns = [
    path('api/products/', ProductApiView.as_view(), name='product-list'),        # GET all, POST
    path('api/products/<int:id>/', ProductApiView.as_view(), name='product-detail'),  # GET, PUT, DELETE
]
