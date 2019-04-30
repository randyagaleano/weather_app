import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=743150ad3eadea636901037ce17ec386'
    city = 'Atlanta'

    res = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : res['main']['temp'],
        'description' : res['weather'][0]['description'],
        'icon': res['weather'][0]['icon'],
    }

    print(city_weather)

    context = {'city_weather' : city_weather}
    return render(request, 'weather/weather.html', context)