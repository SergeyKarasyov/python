#!/usr/bin/env python3

#pip3 install urllib3


import urllib3
from bs4 import BeautifulSoup

def printdata(url):
    req = urllib3.PoolManager()
    res = req.request('GET', url)

    soup = BeautifulSoup(res.data, 'html.parser')
    # print(soup)
    events = soup.find('div', {'id': 'statisticFlat'}).findAll()

    for event in events:
        print(event)
        if(event.find('span').find("priceMkwBrutto")):
            event_details['price'] = event.find('span').find("priceMkwBrutto").text
        # print(event.find())
        # event_details = dict()
        # event_details['name'] = event.find('h3').find("a").text
        # event_details['location'] = event.find('span', {'class', 'event-location'}).text
        # event_details['time'] = event.find('time').text
        print(event_details)

# printdata('https://www.python.org/events/python-events/')
printdata('https://drewnowska43.pl/_get/budynek/3.2/etap/II/pietro/1/nr/m5.6')