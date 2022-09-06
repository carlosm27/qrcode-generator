from django.urls import path
from . import views

urlpatterns = [
    path("qr_bar", views.qr_page, name="qr_bar"),
]