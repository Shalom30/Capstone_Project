from django.urls import path
from book_store_app import views

urlpatterns = [
    path("", views.index, name="index"),
]