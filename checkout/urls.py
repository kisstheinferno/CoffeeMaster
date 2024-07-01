from django.urls import path
from .views import show_checkout

urlpatterns = [
    path("", show_checkout, name="show_checkout"),
]
