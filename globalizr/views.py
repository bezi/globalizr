from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

def about(request):
    return render_to_response('about.html', {'nav': "about"})

def query(request, query="random"):
    print "New query: {}".format(query)
    data = {
        'query': query,
        'error': 0,
    }
    response = json.dumps(data, sort_keys=True)
    return HttpResponse(response, mimetype='application/json')

def home(request):
    return render_to_response('index.html', {'nav': "contact"})
