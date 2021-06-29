import requests
from bs4 import BeautifulSoup

def get_upcoming_events(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')
    listings = soup.find_all('li', attrs={'class': 's-item'})
    print(listings)
    # print(soup)
#     events = soup.find('ul', {'class': 'list-recent-events'}).findAll('li')

#     for event in events:
#         event_details = dict()
#         event_details['name'] = event.find('h3').find("a").text
#         event_details['location'] = event.find('span', {'class', 'event-location'}).text
#         event_details['time'] = event.find('time').text
#         print(event_details)

get_upcoming_events('https://drewnowska43.pl/_get/budynek/1.2/etap/II/pietro/1/nr/m1.4')