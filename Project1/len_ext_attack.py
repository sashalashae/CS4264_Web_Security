import httplib, urlparse, sys
from pymd5 import md5, padding
from urlparse import urlparse

url = "http://courses.cs.vt.edu/cs4264/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp"
toAdd = "&command3=UnlockAllSafes"
parsed = urlparse(url)
query = parsed.query
queryL = query.split('&')
temp = []
name = []
item = []
for i in queryL:
    temp = i.split('=')
    name.append(temp[0])
    item.append(temp[1])

rettoken = md5(state=item[0].decode("hex"), count=512)
rettoken.update(toAdd)
token = rettoken.hexdigest()
'''
end = name[0] + "=" + token + "&" + name[1] + "=" + item[1] + "&" + name[2] + "=" + item[2] + "&" + name[3] + "=" + item[3] + toAdd
nurl = '"' + parsed.scheme + "://" + parsed.netloc + parsed.path + end + toAdd + '"'
url = nurl
print url
'''
# Your code to modify url goes here

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname, parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
