import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import csv

def write_secret(secret):
  # receives (title, description) and writes out to ts_data.csv
  with open('ts_data.csv', 'a', newline='', encoding='utf-8-sig') as file_handler:
    csv_out = csv.writer(file_handler)
    csv_out.writerow(secret)

TITLE_START = 15

secret_id = 0

secrets = []

for x in range(0, 10):
  url = 'https://tusecreto.io/secret/'+str(secret_id)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  title = soup.find('meta', property='og:title')['content'][TITLE_START:]
  description = soup.find('meta', property='og:description')['content']
  write_secret((title, description))
  secret_id += 1
