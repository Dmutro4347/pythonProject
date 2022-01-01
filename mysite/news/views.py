from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('''
                  <h1>Привіт світ</h1>
                  <strong>strong</strong>          
                            ''')


def test(request):
    print(request)
    return HttpResponse('''
                  <h1>ЦЕ тестова сторінка</h1>        
                            ''')

def newurl():