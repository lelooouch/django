import requests
import sqlite3
import json


def send_req(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def parse():
    data_list = list()
    for i in range(1, 83):
        data = send_req(f'https://swapi.dev/api/people/{i}')
        if data:
            data_list.append(data)
    return data_list

def save_data(data):
    with open('data.json', mode = 'w', encoding='utf-8') as file:
        json.dump(data, file)


def update_data(data):
    data_dict = {}
    for index, el in enumerate(data):
        
        el['homeworld'] = send_req(el['homeworld'])['name']

        a = []
        for film in el['films']:
            a.append(send_req(film)['title'])
        el['films'] = a

        a = []
        for specie in el['species']:
            a.append(send_req(specie)['name'])
        el['species'] = a

        a = []
        for vehicle in el['vehicles']:
            a.append(send_req(vehicle)['name'])
        el['vehicles'] = a

        a = []
        for starship in el['starships']:
            a.append(send_req(starship)['name'])
        el['starships'] = a

        data_dict[index] = el

    return data_dict


def main():
    data = parse()
    data = update_data(data)
    save_data(data)


if __name__ == '__main__':
    main()
