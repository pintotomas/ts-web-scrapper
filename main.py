import requests
import helpers
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
UNDEFINED = "undefined"

secret_id = 12129710

for x in range(0, 2000):
  url = 'https://tusecreto.io/secret/'+str(secret_id)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  title = soup.find('meta', property='og:title')['content'][TITLE_START:]
  description = soup.find('meta', property='og:description')['content']
  if UNDEFINED in title and UNDEFINED in description:
    secret_id += 1
    time.sleep(1)
    continue
  gender = helpers.get_gender(title)
  age = helpers.get_age(title)
  write_secret((gender, age, description))
  secret_id += 1
