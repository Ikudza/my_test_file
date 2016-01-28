import sys, os
__file__ = 'test.py'
file = os.path.realpath(__file__).replace('\\', '/')
path = os.path.dirname(file).replace('\\', '/').split('/GAS')[0]

print file
print path

sys.path.append(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SYSTEM.settings')
from django.conf import settings
from django.db import models

from GAS.layer_model import Layer_model
from GAS.models import pipeline

lm = Layer_model('pipeline')
if lm.field_has_choices('p_category'):
    test = lm.get_field_choices('p_category')
    for i in test:
        print i
else:
    print 'lajia'
