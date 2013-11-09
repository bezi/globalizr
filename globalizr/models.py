# Contains functions pertaining to the program's model
import urllib2
import simplejson

def interesting500(y, m, d):
    path = "http://api.flickr.com/services/rest/?"
    path = path + "&method=" + "flickr.interestingness.getList"
    path = path + "&api_key=" + "48dd4e5f2274fe3d6d0793f6e0d92dcc"
    path = path + "&per_page=500"
    path = path + "&date=" + str(y)+"-"
    if (m < 10):
        path = path + "0"
    path = path + str(m) + "-"
    if (d < 10):
        path = path + "0"
    path = path + str(d)
    path = path + "&format=json"
    return path

def interestingMonth(y, m):
    c = []
    for x in xrange(31):
        c.append(interesting500(y,m,x+1))
     return c
#def getGeo(y, m):
#    urls = interestingMonth(y, m)
#    for flickrUrl in urls:
#       req = urllib2.Request(flickrUrl)
#    simplejson.load(opener.open(req))    
