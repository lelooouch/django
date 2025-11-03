from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests


# Create your views here.

def get_luke_info(request):
    response = requests.get('https://swapi.dev/api/people/1/')
    if response.status_code == 200:
        data = response.json()
        return render(request, 'peple/person.html', data)
    return HttpResponse('не удалось')