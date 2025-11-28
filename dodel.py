import requests
import sqlite3
import json

# def send_req(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data
#     return None

# def parse():
#     data_list = list()
#     for i in range(1, 83):
#         data = send_req(f'https://swapi.dev/api/people/{i}')
#         if data:
#             data_list.append(data)
#     return data_list

# def save_data(data):
#     with open('data.json', mode = 'w', encoding='utf-8') as file:
#         json.dump(data, file)

# def update_data(data):
#     data_dict = {}
#     for index, el in enumerate(data):
#         #el['homeworld'] = send_req(el['homeworld'])['name']
#         data_dict[index] = el
#     return data_dict

# def main():
#     data = parse()
#     data = update_data(data)
#     save_data(data)


# if __name__ == '__main__':
#     main()

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS characters(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    height
    mass
    hair_color
    skin_color
    eye_color
    birth_year
    gender
    homeworld
    films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/4/",
            "https://swapi.dev/api/films/5/",
            "https://swapi.dev/api/films/6/"
        ],
        "species": [
            "https://swapi.dev/api/species/2/"
        ],
        "vehicles": [],
        "starships": [],
        "created": "2014-12-10T15:10:51.357000Z",
        "edited": "2014-12-20T21:17:50.309000Z",
        "url
);''')
