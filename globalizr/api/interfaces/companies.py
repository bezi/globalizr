import urllib2
import urllib
import json
import subprocess

def genAllCodes():
    base_url = "http://query.yahooapis.com/v1/public/yql?format=json&env=store%3A%2F%2F\
datatables.org%2Falltableswithkeys&q="
    codes = []
    for industry in range(110, 137):
        print "Industry: {}".format(industry)
        query = "select * from yahoo.finance.industry where id=\"{}\"".format(industry)
        parsed = toJson(base_url, query)
        if not (parsed["query"]["results"]["industry"]["name"] == ""):
            companies = parsed["query"]["results"]["industry"]["company"]
            for company in companies:
                codes.append(company["symbol"])
    return codes

def toJson(baseURL, args):
    args = urllib.quote(args, '')
    req =urllib2.Request(baseURL + args, None)
    opener = urllib2.build_opener()
    f = opener.open(req)
    data = f.read()
    return json.loads(data);

def genStats(code, metric):
    stockStats_base = "http://query.yahooapis.com/v1/public/yql?format=json&env=store%3A%2F%2F\
datatables.org%2Falltableswithkeys&q="
    stock = "select * from yahoo.finance.keystats where symbol=\'" + code + "\'"
    parsed = toJson(stockStats_base, stock)
    if parsed["query"]["results"]["stats"][]
    return parsed["query"]["results"]["stats"]

def genLoc(code):
    city = subprocess.check_output(["./getaddr.sh", code])
    google_geocode_base = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address="
    parsed = toJson(google_geocode_base, city);
    if not (parsed["status"] == "ZERO_RESULTS"):
        return (parsed["results"][0]["geometry"]["location"]["lng"], 
                parsed["results"][0]["geometry"]["location"]["lat"])

def parse_interface_companies(metric):
    codes = genAllCodes();



    for code in codes:
        if genLoc(code) == None:
                
    if metric != "LastTradePriceOnly" || metric != :
        data = genStats()
        if metric == "current price":
            return
        if metric == "total cash":
            return
        if metric == "total debt":
            return
    else:
        data = genQuote(genAllCodes())
        return metric

#print(genQuote("LMT"))
#print(genStats("LMT"))
print(genLoc("LMT") == None)

#print(genQuote("A7Z.DE"))
#print(genStats("A7Z.DE"))
print(genLoc("A7Z.DE") == None)

#print(genQuote("JA9.SI"))
#print(genStats("JA9.SI"))
print(genLoc("JA9.SI") == None)

#print(genQuote("adfadfadf"))
#print(genStats("adfadfadf"))
print(genLoc("adfadfadf") == None)
