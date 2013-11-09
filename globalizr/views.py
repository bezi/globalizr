# Main page views
from django.shortcuts import render_to_response

# Homepage
def home(request):
    return render_to_response('index.html')

#About page
def about(request):
    return render_to_response('about.html')

def world(request):
    return render_to_response('world.html')
