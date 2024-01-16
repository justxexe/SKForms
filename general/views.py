from django.shortcuts import render, get_object_or_404
from .models import Test
import json
from django.http import JsonResponse

def index(request):
    page = 'index.html'
    print(page)
    return render(request, page)

def passTest(request):
    page = 'passTest.html'
    if request.method == 'POST':
        received_data = json.loads(request.body)
        testID = received_data['testId']
        data = {}

        if not testID:
            data['success'] = False
            return JsonResponse(data) 
        
        test = Test.objects.filter(pk=testID).first()
        data = {
            'success' : True,
            'title' : test.title,
            'questions' : test
            }

        return JsonResponse(data) 
        
    return render(request, page)

def test_detail(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    return render(request, 'passTest.html', {'test' : test})

def test_list(request):
    test = Test.objects.all()
    return render(request, 'passTest.html', {'test' : test})