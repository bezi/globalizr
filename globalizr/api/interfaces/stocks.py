import urllib2
import urllib
import json
import os.path
import subprocess
import time

SELF_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_DIRNAME = os.path.join(SELF_PATH, 'json')

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
    try:
        args = urllib.quote(args, '')
        req =urllib2.Request(baseURL + args, None)
        opener = urllib2.build_opener()
        f = opener.open(req)
        data = f.read()
        return json.loads(data)
    except urllib2.HTTPError:
        print("HTTP error. waiting...")
        time.sleep(10)


def genQuote(code, metric):
    stockStats_base = "http://query.yahooapis.com/v1/public/yql?format=json&env=store%3A%2F%2F\
datatables.org%2Falltableswithkeys&q="
    stock = "select * from yahoo.finance.quote where symbol=\'" + code + "\'"
    try:
        parsed = toJson(stockStats_base, stock)
    except urllib2.HTTPError:
        return 0;
    #if parsed["query"]["results"]["quote"]
    return parsed["query"]["results"]["quote"][metric]

def genLoc(code):
    city = subprocess.check_output(["./getaddr.sh", code])
    google_geocode_base = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address="
    parsed = toJson(google_geocode_base, city);
    if not (parsed["status"] == "ZERO_RESULTS"):
        return (parsed["results"][0]["geometry"]["location"]["lat"], 
                parsed["results"][0]["geometry"]["location"]["lng"])

def parse_interface_stocks(metric):
    if metric != "LastTradePriceOnly" and metric != "AverageDailyVolume" and metric != "Change":
        return {"status":1}
    
    codes = genAllCodes();

    data = {
        "name":"stocks",
        "status":0,
        "keys":["default"],
        "data":{
            "default":[]
            },
           
           "metadata":{"default":"The default delimiter"}
        }

    for code in codes:
        print code
        loc = genLoc(code)
        if loc != None:
            quote = genQuote(code, metric)
            data["data"]["default"].append((quote, loc[0], loc[1]))

    return data

def generate():
    f = open(os.path.join(JSON_DIRNAME, "stocks_LastTradePriceOnly.txt"),"w+")
    f.write(parse_interface_stocks("LastTradePriceOnly"))
    f.close()

generate()
