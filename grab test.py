import logging
from grab import Grab
logging.basicConfig(level=logging.DEBUG)
g = Grab()
g.setup(log_dir='log/grab')
g.go('http://yandex.ru')
g.setup(post={'hi':u'Превед,яндекс!'})
g.request()
