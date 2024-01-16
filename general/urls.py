from django.urls import path
from general.views import index, passTest, test_detail

urlpatterns = [
    path('', index, name='home'),
    path('passTest/', passTest, name='passTest'),
    path('test/<int:test_id>/', test_detail, name='test_detail')
]
