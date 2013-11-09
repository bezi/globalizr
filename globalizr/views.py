from django.http import HttpResponse
from django.shortcuts import render_to_response

def about(request):
    return render_to_response('about.html', {'nav': "about"})

def contact(request):
    return render_to_response('contact.html', {'nav': "contact"})

def query(request, query):
    print "New query: {}".format(query)
    data = {
        'query': query,
    }
    response = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

def home(request):
    return render_to_response('index.html', {'nav': "contact"})
