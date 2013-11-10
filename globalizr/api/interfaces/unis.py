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
def curve(x, cap):
    return (math.tanh((cap-x)/(cap/4.0))*20) +30

def getData(infile, cap):
    line = infile.readline()
    idx = 0
    data = []
    while (line != ""):
        print idx
        idx = idx + 1
        t = getLatLong(line.rstrip())
        if (t != "Fail"):
            lat, long = t
            data = data + [curve(idx,cap),lat, long]
        line = infile.readline()
    return data
def generate():
    infiles = [open(os.path.join(JSON_DIRNAME, 'unisartsandhumanities.txt'), 'r'),
               open(os.path.join(JSON_DIRNAME, 'unisengineering.txt'), 'r'),
               open(os.path.join(JSON_DIRNAME, 'unisclinic.txt'), 'r'),
               open(os.path.join(JSON_DIRNAME, 'unislife.txt'),'r'),
               open(os.path.join(JSON_DIRNAME, 'unisscience.txt'), 'r'),
               open(os.path.join(JSON_DIRNAME, 'unissocialsci.txt'), 'r'),
               open(os.path.join(JSON_DIRNAME, 'unis.txt'),'r')]
    outfile =  open(os.path.join(JSON_DIRNAME, 'universities.json'), 'w+')
    keys = ['world', 'artshumanities','engineering','clinical',
             'biology','sciences','history']
    caps = [100, 100, 100, 100, 100, 100, 400]
    data = [0,1,2,3,4,5,6]
    idx = 0
    for infile in infiles: 
        data[idx] = getData(infile, caps[idx])
        idx = idx + 1
    outfile.write('{"name": "universities",\n')
    outfile.write('"status" : 0,\n')
    outfile.write('"keys":'+ str(keys)+',\n')
    outfile.write('"data": {')
    for i in xrange(7):
        outfile.write(keys[i]+':'+str(data[i])+',\n')
    outfile.write('},\n')
    outfile.write('"metadata":')
    descs = '''{ "pasd":  "An integer based on the internationalprestige of a given university, between 0-80.",}\n'''
    outfile.write(descs)
    outfile.write("}\n")
    infile.close()
    outfile.close()

generate()
