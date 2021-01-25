from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index)
]

# now we need to include these urls into the main urls file