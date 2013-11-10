import os.path
import datetime
import urllib2
import json
import re
APPID = 'PThpK43V34HN5z5DoAmlWoqiy72t9Nx_n2qvsMgLY1yBK1uheccHdw6o8eMfDTTtt0zSRBeXpyqNIYz0HvaYmuWjuci0qmI-'
SELF_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_DIRNAME = os.path.join(SELF_PATH, 'json')
""" Evaluates to the Yahoo(TM) WOEID of the given place, evaluates to -1 if query doesn't have a result.
"""
def getWoeid(name):
    path = "http://where.yahooapis.com/v1/places.q(" + str(name) + ");count=1?appid="+str(APPID)+"&format=json"
    req = urllib2.Request(path, None)
    opener = urllib2.build_opener()
    f = opener.open(req)
    places = f.read()
    if 'places' in places:
        db = json.loads(places)
        if 'place' in db['places']:
            if 'woeid' in db['places']['place'][0]:
                return db['places']['place'][0]['woeid']
    return -1
            
def scrape(woeid):
    scraped = {'windchill': '',
               'windspeed': '',
               'humidity': '',
               'pressure': '',
               'lat':'',
               'long':'',
               'high':'',
               'low':''}
    if woeid == -1:
        return scraped
    path = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D"
    path = path + str(woeid)
    path = path + "&format=json"
    req = urllib2.Request(path, None)
    opener = urllib2.build_opener()
    f = opener.open(req)
    tempData = f.read()
    data = json.loads(tempData)
    if 'results' in data['query'] and 'channel' in data['query']['results']:
        
        ch = data['query']['results']['channel']
        if (not 'item' in ch) or (not 'lat' in ch['item']) or (not 'long' in ch['item']):
            return scraped
        if 'wind' in ch:
            scraped["windchill"] = ch['wind']['chill']
            scraped["windspeed"] = ch['wind']['speed']
        if 'atmosphere' in ch:
            scraped["humidity"] = ch['atmosphere']['humidity']
            scraped["pressure"] = ch['atmosphere']['pressure']
        if 'item' in ch:
            scraped['lat'] = ch['item']['lat']
            scraped['long'] = ch['item']['long']
        if 'forecast' in ch['item']:
            scraped['high'] = ch['item']['forecast'][0]['high']
            scraped['low'] = ch['item']['forecast'][0]['low']
    return scraped


def generate():
    infile = open(os.path.join(JSON_DIRNAME, 'capitals.json'), 'r')
    outfile = open(os.path.join(JSON_DIRNAME, 'weather.json'), 'w+')
    line = infile.readline()
    idx = 0
    data = {'windchill':[],
            'windspeed':[],
            'humidity':[],
            'pressure':[],
            'high':[],
            'low':[]}
    while (line != "" and idx < 2000):
        if (idx % 50 == 0): print idx
        idx = idx + 1
        scraped = scrape(getWoeid(line.rstrip()))
        lat = str(scraped['lat'])
        long = str(scraped['long'])
        for k in data.keys():
            if scraped[k] != '':
                data[k].extend([str(scraped[k]),lat,long])
        line = infile.readline()
    outfile.write('{"name": "weather",\n')
    outfile.write('"status" : 0,\n')
    outfile.write('"keys":' + str(data.keys())+',\n')
    outfile.write('"data": {')
    for k in data.keys():
        outfile.write('"'+str(k)+'":'+str(data[k])+",\n")
    outfile.write('},\n')
    outfile.write('"metadata":')
    descs = '''{"windchill": "A measure of the wind's chill",
             "windspeed": "Wind's speed in mph",
             "humidity": "The humidity of the atmosphere",
             "pressure": "Atmospheric pressure for given city",
             "high": "Highest temperature for that day in Fahrenheit",
             "low":  "Lowest temperature for that day in Fahrenheit",}\n'''
    outfile.write(descs)
    outfile.write("}\n")
    infile.close()
    outfile.close()

generate()
