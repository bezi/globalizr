import json

file_in = open('flickr_old.json', 'r')

data = json.loads(file_in.read())

for month in data['data'].keys():
  if month[:5] == 'month':
    length = len(data['data'][month])
    # print 'yes', length
    for i in xrange(length):
      if (i - 1) % 3 == 0:
        # print data['data'][month][i], data['data'][month][i + 1]
        data['data'][month][i], data['data'][month][i + 1] = data['data'][month][i + 1], data['data'][month][i]
        # print data['data'][month][i], data['data'][month][i + 1]
      print '\r' + int((float(i) / length) * 80) * '#',
    print

file_out = open('flickr.json', 'w')
file_out.write(json.dumps(data))
