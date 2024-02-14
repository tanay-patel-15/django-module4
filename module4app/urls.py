from django.urls import path
from . import views

urlpatterns = [
  path("input", views.input),
  path("details", views.details)
]