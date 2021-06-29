# getting the data
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from lxml import etree# get html from site and write to local file
url = 'https://drewnowska43.pl/_get/budynek/4.2/etap/II/pietro/1/nr/m7.2'
headers = {'Content-Type': 'text/html',}
response = requests.get(url, headers=headers)
# print(response.content)
soup = BeautifulSoup(response.content, 'lxml')
print(soup)