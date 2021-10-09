import requests



with open('task3.txt', 'r+', encoding= 'UTF-8') as file:
    APPIDENTIFICATOR = '2d5d685cec99f0a35158bc16f66779ce'
    city = input('Your city')
    REQUEST = requests.get('http://api.openweathermap.org/data/2.5/find', params= {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': APPIDENTIFICATOR})
    json_request = REQUEST.json()

    print(f'Weather temperature in {city}: ', json_request['list'][0]['main']['temp'], '\n',
          'Today minimal temperature was: ', json_request['list'][0]['main']['temp_min'], '\n',
          'Maximum temperature: ', json_request['list'][0]['main']['temp_max'], '\n', 'Temperature feels like: ',
          json_request['list'][0]['main']['feels_like'], sep= '')

