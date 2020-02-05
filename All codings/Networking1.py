import urllib.request
URL = urllib.request.urlopen("https://www.python.org/")
content = URL.read()
URL.close()

createHTML = open("htmlForNetPy.html", "wb")
createHTML.write(content)
createHTML.close()

