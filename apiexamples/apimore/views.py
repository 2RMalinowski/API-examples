import requests
from django.shortcuts import render


def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'apimore/home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'voivodeship': geodata['region_name'],
        'city': geodata['city']
    })
