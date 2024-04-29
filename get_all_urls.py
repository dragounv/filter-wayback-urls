import requests as r
from bs4 import BeautifulSoup, SoupStrainer
import urllib


url = "https://wayback.webarchiv.cz/secure/*/http://www.uloz.to/*"
resp = r.get(url)
soup = BeautifulSoup(resp.text, features="html.parser", parse_only=SoupStrainer('a'))
for link in soup:
    if link.has_attr("href"):
        link = urllib.parse.unquote(link["href"])
        link = str(link).replace(r"%3A", ":")
        link = str(link).replace(r"%2F", "/")
        print(link)