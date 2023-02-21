from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('template-ninja/', template_ninja, name='template_ninja')
]