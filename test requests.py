import requests
t = 'http://10.161.4.65/leaflet/get_towers_new.php'
q = requests.get(t)
tt = 'http://10.161.4.65/leaflet/get_tower_data.php?tower_index='
r = requests.get(tt+'1')
