# Flickr API querying 
import urllib2
import json
import re
import os.path
API_KEY = "48dd4e5f2274fe3d6d0793f6e0d92dcc"
days = [31,28,31,30,31,30,31,31,30,31,30,31]
class Flickr:
    @staticmethod
    def daily_interesting(num, year, month, day):
        print "daily_interesting: "
        print num, year, month, day
        if days[month - 1] < day:
            return []
        path = "http://api.flickr.com/services/rest/?"
        path = path + "&method=" + "flickr.interestingness.getList"
        path = path + "&api_key=" + API_KEY 
        path = path + "&per_page=" + str(num)
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
    @staticmethod
    def geolocPath(photoId):
        path = "http://api.flickr.com/services/rest/?"
        path = path + "&method=" + "flickr.photos.geo.getLocation"
        path = path + "&api_key=" + API_KEY
        path = path + "&photo_id=" + photoId
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

        return (data["photo"]["location"]["longitude"], data["photo"]["location"]["latitude"])
    @staticmethod
    def interestingMonth(year, month):
        locations = []
        for day in xrange(31):
            print "day: {}".format(day)
            i = 0
            for photo_id in Flickr.daily_interesting(500, year, month, day + 1):
                print "{}".format(i)
                i = i + 1
                loc_string = Flickr.geolocPath(photo_id)
                if not (loc_string == "Error: not found"):
                    long = int(float(loc_string[0])*1000)/1000.0
                    lat = int(float(loc_string[1])*1000)/1000.0
                    locations.append((5,long,lat))
        return locations

    @staticmethod
    def parse_interface_flickr(year, month, metric):
        if metric == "interesting":
            locs = Flickr.interestingMonth(year,month)
            data = {
                "status": 0,
                "data": {
                    "name": "Interesting flickr pictures by location.",
                    "data": []
                    }
                }
            for loc in locs:
                data["data"]["data"].append(loc[0])
                data["data"]["data"].append(loc[1])
                data["data"]["data"].append(loc[2])
        else:
            data = { "status": 1 }

        return data

