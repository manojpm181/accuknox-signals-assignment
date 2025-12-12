from django.urls import path
from . import views

urlpatterns = [
    path("rectangle/", views.rectangle_view, name="rectangle"),
    path("signals/", views.signal_test_view, name="signals"),
    path("test/", views.test_view, name="test"),
]
