from django.urls import path
from .views import frontpage, basepage



urlpatterns = [
    path('',basepage, name='basepage'),
    path('frontpage/',frontpage, name='frontpage'),
]
