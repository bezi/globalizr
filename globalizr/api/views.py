# API views
import os
import json
from query import parse_query
from interfaces.flickr import parse_interface_flickr
from django.http import HttpResponse

INTERFACE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/interfaces/json/'
INTERFACES = ["flickr", "weather", "universities"];
def interface(request, inter, disc="default"):
    print "SHIT GOT CALLED {}".format(inter)
    if inter.lower() in INTERFACES:
        print "WE ARE GOOD TO FUCKING GO"
        response = open(INTERFACE_DIR + inter.lower() + '.json').read()
    else:
        print "FUCKIN {} AINT IN {}".format(inter, INTERFACES)
        data = { "status": 1, "key": inter }
        response = json.dumps(data, sort_keys=True)
    return HttpResponse(response, mimetype='application/json')

def error(request):
    response = {"error": "faulty API call"}
    return HttpResponse(json.dumps(response), mimetype='application/json')
