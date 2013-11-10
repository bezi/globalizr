import os.path
import datetime
import urllib2
import json
import re
import math
APPID = 'PThpK43V34HN5z5DoAmlWoqiy72t9Nx_n2qvsMgLY1yBK1uheccHdw6o8eMfDTTtt0zSRBeXpyqNIYz0HvaYmuWjuci0qmI-'
SELF_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_DIRNAME = os.path.join(SELF_PATH, 'json')
""" Evaluates to the Yahoo(TM) WOEID of the given place, evaluates to -1 if query doesn't have a result.
"""
def getLatLong(name):
    path = "http://where.yahooapis.com/v1/places.q(" + str(name) + ");count=1?appid="+str(APPID)+"&format=json"
    req = urllib2.Request(path, None)
    opener = urllib2.build_opener()
    f = opener.open(req)
    places = f.read()
    if 'places' in places:
        db = json.loads(places)
        if 'place' in db['places'] and len(db['places']['place']) > 0:
            if 'centroid' in db['places']['place'][0]:
                return db['places']['place'][0]['centroid']['latitude'], db['places']['place'][0]['centroid']['longitude']
    return "Fail"
#simulates arctan
def curve(x):
    return (math.tanh((200-x)/50.0)+1)*40

def generate():
    infile = open(os.path.join(JSON_DIRNAME, 'unis.txt'), 'r')
    outfile = open(os.path.join(JSON_DIRNAME, 'universities.json'), 'w+')
    line = infile.readline()
    idx = 0
    data = []
    while (line != ""):
        print idx
        idx = idx + 1
        t = getLatLong(line.rstrip())
        if (t != "Fail"):
            lat, long = t
            data = data + [curve(idx),lat, long]
        line = infile.readline()
    print data
    outfile.write('{"name": "universities",\n')
    outfile.write('"status" : 0,\n')
    outfile.write('"keys": "points",\n')
    outfile.write('"data": {')
    outfile.write('"points":'+str(data)+"\n")
    outfile.write('},\n')
    outfile.write('"metadata":')
    descs = '''{ "points":  "An integer based on the internationalprestige of a given university, between 0-80.",}\n'''
    outfile.write(descs)
    outfile.write("}\n")
    infile.close()
    outfile.close()

generate()
