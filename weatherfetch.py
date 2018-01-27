#!/usr/bin/env python
#author: matthew smith
#github: github.com/paumanok


import urllib2
import json

import weatherconfig #config file to hold area and api info

debug = True

weather_data = { 'temp_f': None,
                 'temp_c': None,
                 'fcttext': None,
                 }

# fetch data gets the current temp in a location
#should add forcast functionality later
def fetch_conditions_data():
    url = "http://api.wunderground.com/api/f8ca379fcb9f0181/conditions/q/" \
            + weatherconfig.state + '/' + weatherconfig.city + ".json"
    if debug:
        print("fetching from "+ url + '\n')

    data = urllib2.urlopen(url)
    json_data = data.read()
    parsed_json = json.loads(json_data)
    return parsed_json

def fetch_forecast_data():

    url = "http://api.wunderground.com/api/f8ca379fcb9f0181/forecast/q/" \
            + weatherconfig.state + '/' + weatherconfig.city + ".json"

    if debug:
        print("fetching from "+ url + '\n')

    data = urllib2.urlopen(url)
    json_data = data.read()
    parsed_json = json.loads(json_data)
    return parsed_json


def get_weather():
    conditions_data = fetch_conditions_data()
    #forecast_data = fetch_forecast_data()

    weather_data['temp_f'] = conditions_data['current_observation']['temp_f']
    weather_data['temp_c'] = conditions_data['current_observation']['temp_c']
    #weather_data['fcttext'] = forecast_data['forecast']['txt_forecast']['forecastday'][0]['fcttext']
    return weather_data

def printweather():
    get_weather()

    print("temp in f " + str(weather_data['temp_f']) + '\n')
    print("todays forcast: " + weather_data['fcttext'] + '\n' )


#if(debug):
 #:   printweather()
#get_weather()
