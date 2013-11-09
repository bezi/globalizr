# API views
import json
from query import parse_query
from django.http import HttpResponse

# Query for a search string, returns JSON representing 
# globe data
def query(request, query="random"):
    print "New query: {}".format(query)
    data = parse_query(query)
    response = json.dumps(data, sort_keys=True)
    return HttpResponse(response, mimetype='application/json')
