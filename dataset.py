import json
import urllib.request


def refresh():
    with urllib.request.urlopen("https://data.austintexas.gov/resource/3kfv-biw6.json?$limit=99999999") as url:
        save(json.loads(url.read().decode()))


def load():
    with open('dataset.json', 'r') as file:
        return json.loads(file.read())


def save(data):
    with open('dataset.json', 'w') as file:
        json.dump(data, file)