from django.urls import path
from .views import category, product


urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>', product, name='product'),
    path('<slug:category_slug>/', category, name='category'),
]
