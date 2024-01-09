from django.shortcuts import render
from .models import Test
import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    page = 'index.html'
    print(page)
    return render(request, page)

def passTest(request):
    page = 'passTest.html'
    if request.method == 'POST':
        received_data = json.loads(request.body)
        testId = received_data['testId']
        print(Test.objects.all()[testId])
        data = {
            "asd" : '1123',
            'zxc' : 'chadow fint'
        }

        return JsonResponse(data) 
        
    return render(request, page)

def test_detail(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    return render(request, 'passTest.html', {'test': test})
