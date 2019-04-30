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

    return render(request, 'weather/weather.html')

    # response object for hard-coded city
    # {"coord":
    #     {
    #         "lon":-84.39,
    #         "lat":33.75
    #     },
    #     "weather":
    #         [{"id":800,
    #         "main":"Clear",
    #         "description":"clear sky",
    #         "icon":"01d"}],
    #     "base":"stations",
    #     "main":
    #         {"temp":77.18,
    #         "pressure":1024,
    #         "humidity":69,
    #         "temp_min":73,
    #         "temp_max":82},
    #     "visibility":16093,
    #     "wind":
    #         {"speed":3.94,
    #         "deg":142.921},
    #     "clouds":
    #         {"all":1},
    #     "dt":1556639005,
    #     "sys":
    #         {"type":1,
    #         "id":4155,
    #         "message":0.0111,
    #         "country":"US",
    #         "sunrise":1556621396,
    #         "sunset":1556669967},
    #     "id":4180439,"name":"Atlanta",
    #     "cod":200
    # }