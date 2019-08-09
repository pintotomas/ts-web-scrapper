import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
print(urlopen)
url = "https://tusecreto.io/secret/2342"
response = requests.get(url)
print(response)