import httplib, urlparse, sys
import urllib
from pymd5 import md5, padding

url = sys.argv[1]
# Your code to modify url goes here

##########################################################################

tokenStart = url.find("=")
tokenStop = url.find("&")

urlPt1 = url[ : tokenStart + 1]
origToken = url[tokenStart + 1 : tokenStop]
origMsg = url[tokenStop : ]

toAdd = "&command3=UnlockAllSafes"

origLen = len(origMsg) - 1 + 8
origPad = padding(origLen*8)

h = md5(state=origToken.decode("hex"), count=512)
h.update(toAdd)
newToken = h.hexdigest()

modURL = urlPt1 + str(newToken) + origMsg

readablePad = urllib.quote(origPad)

url = modURL + str(readablePad) + toAdd

print("New URL: " + url)

##########################################################################

parsedUrl = urlparse.urlparse(url)
conn = httplib.HTTPSConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()