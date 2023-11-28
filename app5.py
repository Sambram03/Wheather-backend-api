from flask import Flask, request, jsonify
import requests

app = Flask(_name_)

API_KEY = '80edfa30c1710d24ec8ea0bae32ee47c'  # Replace with your API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    params = {
        'q': city,
        'appid': API_KEY,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify({
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
        })
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), response.status_code

if _name_ == '_main_':
    app.run(debug=True)