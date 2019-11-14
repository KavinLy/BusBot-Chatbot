url = "https://nxbus.co.uk/routes/coventry/"

from bs4 import BeautifulSoup
from urllib.request import urlopen
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
routeNumber = soup.find('span', {'class': 'route-number'}).text
routeTo = soup.find('td', {'class': 'main_and_via'})
destination = routeTo.find('a').text
via = routeTo.find('span', {'class': 'via'}).text
via = via[3:len(via)]
via = via[0:4] + ':' + via[4:len(via)]

print("Route number: " + routeNumber, "  Destination: " + destination, via)
