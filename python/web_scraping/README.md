# Let's get some of the basics out of the way

A uniform resource locator (URL) is a string that holds a lot of information. A typical URL could have the form ```https://en.wikipedia.org/wiki/URL?key=value&life=42#History```, 

- At the beginning we have the **protocol** (```https```) sometimes called a **scheme**
- Next **hostname** (```en.wikipedia.org```) sometimes following by ```:port```. If the port is not explicitly specified, this can be determined from the protocol ```http=80``` and ```https=443```
- After, comes the **path** (```wiki/URL```).
- The text after the ```?``` is called the **Querystring**. This holds a collection of key value pairs seperated by ```&```
- Lastly, a ```#``` followed by a string could be included at the end. This value is called a **fragment** and is used to jump to a section within the webpage

## urllib
urllib is a package that collects several modules for working with URLs:
- [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) for opening and reading URLs
- urllib.response used internally by the request module
- [urllib.error](https://docs.python.org/3/library/urllib.error.html#module-urllib.error) containing the exceptions raised by [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
- [urllib.parse](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse) for parsing URLs into individual parts
- [urllib.parse](https://docs.python.org/3/library/urllib.robotparser.html#module-urllib.robotparser) for parsing robots.txt files for what permissions are granted to bots and crawlers