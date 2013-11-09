from django.shortcuts import render_to_response

# Homepage
def home(request):
    return render_to_response('index.html', {'nav': "contact"})

#About page
def about(request):
    return render_to_response('about.html', {'nav': "about"})

