from django.urls import path

from .views import ProductDetailView, ProductListView, ProductAddNew, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='home'),
    path('product/new/', ProductAddNew.as_view(), name='product_new'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]
