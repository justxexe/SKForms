from django.urls import path
from general.views import index, passTest

urlpatterns = [
    path('', index, name='home'),
    path('passTest/', passTest, name='passTest')
]
