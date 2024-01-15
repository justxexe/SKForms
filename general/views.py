from django.shortcuts import render
from .models import Test
import json
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    page = 'index.html'
    print(page)
    return render(request, page)

def passTest(request):
    page = 'passTest.html'
    if request.method == 'POST':
        received_data = json.loads(request.body)
        test = Test.objects.all()[received_data['testId']]
        data = {'asdasd' : 'asdasd'}

        return JsonResponse(data) 
        
    return render(request, page)
