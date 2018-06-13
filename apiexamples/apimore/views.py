import requests
from django.conf import settings
from django.shortcuts import render


def geo(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'apimore/geo.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'voivodeship': geodata['region_name'],
        'city': geodata['city'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': settings.API_KEY,
    })



