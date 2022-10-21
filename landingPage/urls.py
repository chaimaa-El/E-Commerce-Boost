from django.urls import path
from landingPage import views

app_name = 'landingPage'

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
]
