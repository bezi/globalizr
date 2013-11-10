import os.path
from flickr import *
import datetime

SELF_PATH = os.path.dirname(os.path.abspath(__file__))
JSON_DIRNAME = os.path.join(SELF_PATH, 'json')
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def generateJSON(year, month, metric):
    data = parse_interface_flickr(year, month, metric)
    n = ('"'+"Popular Flickr pictures for " + months[month-1]+" "+str(year)+'"')
    s = data["status"]
    pos_data_name = data["data"]["name"]
    pos_data = data["data"]["data"]
    result = '    "name": '+n+',\n'
    result = result + '    "status": ' + str(s)+',\n'
    result = result + '    "pos_data": {\n'
    result = result + '        "name":' + pos_data_name +',\n'
    result = result + '        "data":' + str(pos_data) +',\n'
    result = result + '    }\n'
    return result


def generate():
    metric = "interesting"
    id = 0
    
    f = open(os.path.join(JSON_DIRNAME, "flickr_"+metric+".txt"),"w+")
    f.write('{ "name": "Popular pictures in Flickr by location",\n')
    f.write('"status": 0, \n')
    f.write('"data": {\n')
    year = datetime.datetime.today().year - 1
    month = datetime.datetime.today().month
    print year
    print " "
    print month
    for x in xrange(12):
        f.write('"month'+str(id)+'": {\n')
        f.write(generateJSON(year, month + 1, metric))
        id = id + 1
        if (month >= 11):
            month = 0
            year = year + 1
        else: month = month + 1
        f.write('}')
    f.write('}')
    f.close()

generate()
