from django.urls import path
from goods import views

urlpatterns = [
    path('register/', views.register)
]

