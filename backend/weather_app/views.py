import requests
from django.shortcuts import render
from .forms import WeatherForm

# Create your views here.
def get_weather_data(city):
    api_key = API_KEY
    base_url = BASE_URL
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def weather(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
            
            if weather_data['cod'] == 200:
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                context = {'temperature': temperature, 'description': description, 'city': city}
            else:
                context = {'error_message': 'City not found'}
            
            return render(request, 'weather_app/weather.html', context)
    else:
        form = WeatherForm()

    return render(request, 'weather_app/weather.html', {'form': form})