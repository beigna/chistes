import requests


def joke_chuck():
    url = 'https://api.chucknorris.io/jokes/random'
    res = requests.get(url, headers={'Accept': 'application/json'})
    return res.json()['value']


def joke_dad():
    url = 'https://icanhazdadjoke.com'
    res = requests.get(url, headers={'Accept': 'application/json'})
    return res.json()['joke']
