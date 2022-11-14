from django.urls import path

from . import views

urlpatterns = [path("data", views.DummyView.as_view())]
