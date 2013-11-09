# Contains functions pertaining to the program's model
import urllib2
import json
import re

API_KEY = "48dd4e5f2274fe3d6d0793f6e0d92dcc"

def daily_interesting(year, month, day):
    path = "http://api.flickr.com/services/rest/?"
    path = path + "&method=" + "flickr.interestingness.getList"
    path = path + "&api_key=" + API_KEY 
    path = path + "&per_page=500"
    path = path + "&date=" + str(year)+"-"
    if (month < 10):
        path = path + "0"
    path = path + str(month) + "-"
    if (day < 10):
        path = path + "0"
    path = path + str(day)
    path = path + "&format=json"

    req = urllib2.Request(path, None)
    opener = urllib2.build_opener() 
    f = opener.open(req)
    photos = f.read()
    response_parser = re.compile(r'jsonFlickrApi\((.*?)\)$')
    parsed_photos = response_parser.findall(photos)
    data = json.loads(parsed_photos[0])
    
    ids = []
    for photo in data["photos"]["photo"]:
        ids.append(photo["id"])
       
    return ids

def geolocPath(photoId):
    path = "http://api.flickr.com/services/rest/?"
    path = path + "&method=" + "flickr.photos.geo.getLocation"
    path = path + "&api_key=" + API_KEY
    path = path + "&photo_id={}".format(photoId)
    path = path + "&format=json"

    req = urllib2.Request(path, None)
    opener = urllib2.build_opener()
    f = opener.open(req)
    location = f.read()
    response_parser = re.compile(r'jsonFlickrApi\((.*?)\)$')
    parsed_location = response_parser.findall(location)

    data = json.loads(parsed_location[0])
    if data["stat"] == "fail":
        return "Error: not found"

    return (data["photo"]["location"]["latitude"], data["photo"]["location"]["longitude"])

def interestingMonth(year, month):
    locations = []
    for day in xrange(31):
        for photo_id in daily_interesting(year, month, day + 1):
            loc_string = geolocPath(photo_id)
            if not (loc_string == "Error: not found"):
                locations.append(loc_string)    
    return locations
