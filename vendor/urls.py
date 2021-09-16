from django.urls import path
from django.contrib.auth import views as auth_views
from .views import become_vendor, vendor_admin, add_product

urlpatterns = [

    path('become-vendor/', become_vendor, name='become_vendor'),
    path('vendor-admin/', vendor_admin, name='vendor_admin'),
    path('add_product/', add_product, name='add_product'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
