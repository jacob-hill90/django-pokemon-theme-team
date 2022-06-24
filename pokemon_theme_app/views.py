from django.http import HttpResponse
from django.shortcuts import render
import requests
import random

def index(request):
    return render(request, 'index.html')















# def get_pokemon(request):
#     rand_num = random.randint(1, 898)
#     API_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{rand_num}/')
#     responseJSON = API_response.json()
#     name = responseJSON['name']
#     photo = responseJSON['sprites']['front_default']
#     # type = 
#     # response = render(request, 'pages/index.html', {'name': , 'some-other-data': 4})
#     print(responseJSON['types'][0]['type'])
