import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
import csv


url = 'https://tusecreto.io/secret/12133584'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('meta', property='og:title')['content'][15:]
description = soup.find('meta', property='og:description')['content']

secrets = [(title, description)]

with open('ts_data.csv', 'w') as file_handler:
	csv_out = csv.writer(file_handler)
	csv_out.writerow(['titulo', 'secreto'])
	for row in secrets:
		csv_out.writerow(row)
