from django.shortcuts import render, get_object_or_404
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=36e273f8799f1fa7da3877a97905d835'
    
    cities = City.objects.all()
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = CityForm()
    weather_data = []
    
    
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
    
        weather = {
            'city' : city,
            'temperature' : round((city_weather['main']['temp']-32)*5/9, 1),
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        print(weather)
        weather_data.append(weather)
        
    context = {'weather_data' : weather_data, 'form' : form}
    
    return render(request, 'weather/index.html', context)

def detail(request, weather_id):
    weather = get_object_or_404(City, pk=weather_id)
    return render(request, 'detail.html', {'weather':weather})