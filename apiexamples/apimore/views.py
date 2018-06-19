import requests
from django.conf import settings
from django.shortcuts import render
from .forms import DictionaryForm


def geo(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('http://freegeoip.net/json/%s' % ip_address)
        request.session['geodata'] = response.json()

    geodata = request.session['geodata']

    return render(request, 'apimore/geo.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'voivodeship': geodata['region_name'],
        'city': geodata['city'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': settings.API_KEY,
        'is_cached': is_cached
    })


def oxford(request):
    search_result = {}
    if 'word' in requests.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'core/oxford.html', {'form': form, 'search_result': search_result})
