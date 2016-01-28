import requests


def cicle(dicts, gkey):
    try:
        keys = dicts.keys()
        if keys:
            print gkey, keys
            for key in keys:
                cicle(dicts[key], key)
    except:
        try:
            keys = dicts[0].keys()
            if keys:
                print gkey, keys
                for key in keys:
                    cicle(dicts[0][key], key)
        except:
            print gkey, dicts
            pass

api_key = '7c7760a77d7f5334b08c3e695b927'
type_weather = {}
type_weather['local'] = 'weather.ashx'
# type_weather['past'] = 'past-weather.ashx'
# type_weather['point'] = 'ski.ashx'


for key in type_weather.keys():
    url = 'http://api.worldweatheronline.com/free/v2/%s' % type_weather[key]

    city = {}
    city['name'] = '?q='
    city['id'] = 'city?id='
    future = '&num_of_days=%s' % 5
    format_ = '&format=json'
    api = '&key=%s' % api_key
    name = 'Rostov-on-Don'
    options = city['name'] + name + format_ + api

    q = requests.get(url + options)

    datas = q.json()

    cicle(datas, key.upper())
