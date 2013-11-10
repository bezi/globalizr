# API views
import os
import json
from query import parse_query
from interfaces.flickr import parse_interface_flickr
from django.http import HttpResponse

INTERFACE_DIR = os.path.abspath(os.path.dirname(__file__)) + '/interfaces/json/'
INTERFACES = ["flickr", "weather"];
def interface(request, interface, disc="default"):
    if interface.lower() in INTERFACES:
        response = open(INTERFACE_DIR + interface.lower() + '.json').read()
    else:
        data = { "status": 1 }
        response = json.dumps(data, sort_keys=True)
    return HttpResponse(response, mimetype='application/json')

def error(request):
    response = {"error: faulty API call"}
    return HttpResponse(json.dumps(response), mimetype='application/json')
