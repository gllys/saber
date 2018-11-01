from django.urls import path
from operate.login.views import *

urlpatterns = [
    path('login/', login),
]
