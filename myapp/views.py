from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def testfctn(request):
    return HttpResponse('hai')
def testfctn1(request):
    return HttpResponse('heloo')
def test(request):
    return render(request,'test.html') 
def test2(request):
    return render(request,'form.html')            