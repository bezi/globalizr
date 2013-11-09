# API views
import json
from query import parse_query
from interfaces.flickr import parse_interface_flickr
from django.http import HttpResponse

# Query for a search string, returns JSON representing 
# globe data
def query(request, query="random"):
    data = parse_query(query)
    response = json.dumps(data, sort_keys=True)
    return HttpResponse(response, mimetype='application/json')

def interface(request, interface="random", metric="random"):
    if interface == "flickr":
        data = parse_interface_flickr(metric)
    else:
        data = { "status": 1 }
    response = json.dumps(data, sort_keys=True)
    return HttpResponse(response, mimetype='application/json')
