from django.urls import path
from .views import calculate

urlpatterns = [
    path('calculate/<str:operation>/<int:num1>/<int:num2>/', calculate)
]