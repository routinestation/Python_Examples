# This code is based on https://www.youtube.com/watch?v=dyUhGZ6iNTc

import requests, sys, webbrowser, bs4

res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElements = soup.select(r'a')
linkToOpen = min(6, len(linkElements))
for i in range(linkToOpen):
    webbrowser.open('https://google.com'+linkElements[i].get('href'))