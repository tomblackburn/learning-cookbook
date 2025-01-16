# https://docs.python.org/3/library/urllib.html
# urllib is a package that collects several modules for working with URLs

from urllib.request import Request, urlopen # for opening and reading URLs
from urllib.parse import urlparse, urlencode

# Open URL with string containing a valid, properly encoded URL
response = urlopen("http://python.org")
print(response.status)
print(response.reason)

# The response is not a string, but a bytes object indicated by the b at the beginning
# Web servers can host binary data, in addition to plain html files
data = response.read()
print(type(data))
print(len(data))
#html = data.decode("UTF-8")
#print(type(html))
#print(html)


print("--------------------------------------------------")

# Prebuild the request
request = Request("http://python.org")

# headers can be added as through the constructor
# headers should be a dictionary, and will be treated as if add_header() was called with each key and value as arguments.
# This is often used to “spoof” the User-Agent header value, which is used by a browser to identify itself
# Some HTTP servers only allow requests coming from common browsers as opposed to scripts. 
request.add_header("User-Agent", "Not Firefox")
print(urlopen(request).peek())

# Parse a URL into six components, returning a 6-item named tuple.
# This corresponds to the general structure of a URL: scheme://netloc/path;parameters?query#fragment
parsed_url = urlparse(
    "https://python.org/test/node/1?q=1&x=that#test_fragment")

print("--------------------------------------------------")

print(parsed_url)
print(parsed_url.scheme)    # URL scheme specifier
print(parsed_url.netloc)    # Network location part
print(parsed_url.path)      # Hierarchical path
print(parsed_url.params)    # Parameters for last path element
print(parsed_url.query)     # Query component
print(parsed_url.fragment)  # Fragment identifier

# As is the case with all named tuples, the subclass has a few additional methods and attributes that are particularly useful. 
# One such method is _replace(). The _replace() method will return a new ParseResult object replacing specified fields with new values.
parsed_url._replace(scheme='http')
print(parsed_url.scheme)

# This URL contains 2 parameters in the querystring
# v is the video id and t is the time begin playback
yt = "https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s"
# One way to construct the query string is to concatenate various data together
qs = "v=" + "EuC-yVzHhMI" + "&" + "t=" + "5m56s"

# A better way is to create a dictionary containing the query string parameters
params = {"v": "EuC-yVzHhMI",
          "t": "5m56s"}
querystring = urlencode(params)
print(querystring) # notice the ? is not included
url = "https://youtube.com/watch" + "?" + querystring
resp = urlopen(url)
print(resp.isclosed()) # Check if we still have a connection with the server
html = resp.read().decode("utf-8")
print(html[:500])