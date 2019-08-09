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

MALE = "hombre"
MALE_SYMBOL = "H"
FEMALE = "mujer"
FEMALE_SYMBOL = "M"

def get_gender(secret_title):
  if MALE in secret_title:
    return MALE_SYMBOL
  elif FEMALE in secret_title:
    return FEMALE_SYMBOL
  else:
    return "undefined"

AGE_START = -7
AGE_END = -5

def get_age(secret_title):
  return secret_title[AGE_START:AGE_END]

TITLE_START = 15
UNDEFINED = "undefined"

secret_id = 0

secrets = []

for x in range(0, 10):
  url = 'https://tusecreto.io/secret/'+str(secret_id)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  title = soup.find('meta', property='og:title')['content'][TITLE_START:]
  description = soup.find('meta', property='og:description')['content']
  if UNDEFINED in title and UNDEFINED in description:
    secret_id += 1
    time.sleep(1)
    continue
  gender = get_gender(title)
  age = get_age(title)
  write_secret((gender, age, description))
  secret_id += 1
