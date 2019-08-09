import requests
import helpers
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import csv
import sys

def save_secret(secret):
  # receives (title, description) and writes out to ts_data.csv
  with open('ts_data.csv', 'a', newline='', encoding='utf-8-sig') as file_handler:
    csv_out = csv.writer(file_handler)
    csv_out.writerow(secret)


TITLE_START = 15
UNDEFINED = "undefined"
STARTING_SECRET = 1
if __name__ == '__main__':
  if(len(sys.argv) == 2):
    if (sys.argv[STARTING_SECRET].split("=")[0]=="start"):
      secret_id = int(sys.argv[STARTING_SECRET].split("=")[1])

  else:
    print("Saving from secret with ID 0. You can specify the id running python main.py start=XX")
    secret_id = 0
  print("Starting from: "+str(secret_id))
  for x in range(0, 5000):
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
    save_secret((gender, age, description))
    secret_id += 1



