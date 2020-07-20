from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests

    url  = 'http://api.weatherstack.com/current?access_key=2feca4577cea09842ad41b06930b3e61&query=Lucknow'
    air_url = 'http://api.airpollutionapi.com/1.0/aqi?lat=26.850000&lon=80.949997&APPID=l1u04hr351o6f3vqitk0iaen2o'


    try:
        api = requests.get(url).json()
        air_api = requests.get(air_url).json()

    except Exception as e:
        api = print(e)


    if air_api['data']['text'] == "Good":
            category_color = "Good"
    elif air_api['data']['text'] == "Satisfactory":
        category_color = "Satisfactory"
    elif air_api['data']['text'] == "Moderate":
        category_color = "Moderate"
    elif air_api['data']['text'] == "Poor":
        category_color = "Poor"
    elif air_api['data']['text'] == "VeryPoor":
        category_color = "VeryPoor"
    elif air_api['data']['text'] == "Severe":
        category_color = "Severe"

    return render(request, 'home.html', {'api':api,'air_api':air_api,'category_color':category_color})
























def about(request):
    return render(request , 'about.html')
