import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=743150ad3eadea636901037ce17ec386'
    # city = 'Atlanta'

    if request.method == 'POST':
        pass 

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
    
        res = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : res['main']['temp'],
            'description' : res['weather'][0]['description'],
            'icon': res['weather'][0]['icon'],
        }

        weather_data.append(city_weather)
        
    print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)