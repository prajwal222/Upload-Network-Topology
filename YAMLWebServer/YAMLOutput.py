'''
from django.core import serializers
from pprint import pprint
def printYAML(value):
    from pprint import pprint
    pprint(serializers.serialize('yaml',value, fields =('hostname','host','username','password','device_type')))

'''

import yaml
from YAMLDatabase.models import *

j = 0
def createYAML(data):
    global j
    from django.core import serializers
    from pprint import pprint
    #data = YAMLEntry.objects.all()

    print("Heya")
    i = data
    dict_file = [{'hostname': i.hostname}, {'host': i.host}, {'username': i.username}, {'password': i.password},
                 {'device_type': i.device_type}]

    with open("output1.yaml", 'w') as file:
            yaml.dump(dict_file, file)

    j+=1
    return i.hostname



