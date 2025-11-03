from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests


# Create your views here.
def send_req(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    return None

def update_data(data):
    films = data['films']
    vehicles = data['vehicles']
    starships = data['starships']

    new_films = list()
    for film in films:
        film = send_req(film)
        new_films.append(film['title'])

    new_vehicles = list()
    for vehicle in vehicles:
        vehicle = send_req(vehicle)
        new_vehicles.append(vehicle['name'])

    new_starships = list()
    for starship in starships:
        starship = send_req(starship)
        new_starships.append(starship['name'])

    data['films'] = new_films
    data['vehicles'] = new_vehicles
    data['starships'] = new_starships

    return data

def get_luke_info(request):
    data = send_req('https://swapi.dev/api/people/1/')
    if data:
        updated_data = update_data(data)

        return render(request, 'peple/person.html', updated_data)
    return HttpResponse('не удалось')
