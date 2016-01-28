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
            print len(dicts)
            if keys:
                print gkey, keys
                for key in keys:
                    cicle(dicts[1][key], key)
        except:
            # print gkey, dicts
            pass

api_key = '8eb9ca1f82846e43710de014aba0e146'
url = 'https://api.forecast.io/forecast/'
coord = '48.0383, 40.2636'
api = '%s/' % api_key
options = api + coord + '?units=si&lang=ru'

q = requests.get(url + options)

datas = q.json()

# cicle(datas, '!')
print datas