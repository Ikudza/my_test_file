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
            keys = dicts[1].keys()
            if keys:
                print gkey, keys
                for key in keys:
                    cicle(dicts[1][key], key)
        except:
            print gkey, dicts
            pass


api_key = 'b4df0968d6edbc700b972366b6fddf25'
url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
x = '48.0383'
y = '40.2636'
coord = '?lat=%s&lon=%s&units=metric&lang=ru' % (x, y)
api = '&APPID={%s}' % api_key
name = 'Rostov-on-Don'

# options = city['name'] + name + api
options = coord + api

q = requests.get(url + options)

datas = q.json()

# cicle(datas, '!')
print datas
