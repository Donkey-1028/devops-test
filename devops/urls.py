from django.urls import path

from .views import Home


app_name = 'devops'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]