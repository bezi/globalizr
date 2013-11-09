import urllib2
import urllib
import json

def genAllCodes():
    base_url="http://query.yahooapis.com/v1/public/yql?format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&q="
    codes = []
    for industry in range(110, 137):
        print "Industry: {}".format(industry)
        query = "select * from yahoo.finance.industry where id=\"{}\"".format(industry)
        query = urllib.quote(query, '')
        req = urllib2.Request(base_url + query, None)
        opener = urllib2.build_opener()
        f = opener.open(req)
        data = f.read()
        parsed = json.loads(data);
        if not (parsed["query"]["results"]["industry"]["name"] == ""):
            companies = parsed["query"]["results"]["industry"]["company"]
            for company in companies:
                codes.append(company["symbol"])
    return codes

print len(genAllCodes())
