from bs4 import BeautifulSoup
from urllib.request import urlopen

line13Url = "https://www.networkwestmidlands.com/plan-your-journey/timetables#/route/cen_41013_C_H_y11_14-14"
line8Url = "..."
selectedLineUrl = ""

#scan which_line thing that you did the other time

which_line = input("Which bus line would you like to know? ")

if which_line == "13":
  selectedLineUrl = line13Url
elif which_line == "8":
  selectedLineUrl = line8Url

selecLineUrl = urlopen(selectedLineUrl)
soup = BeautifulSoup(selecLineUrl, "html.parser")
stops = soup.findAll("a", {"class": "journey-link"})
stopsData = []

for stop in stops:
  stopData = BeautifulSoup(stop["href"], "html.parser")
  stopsData.append({"stopName": stopData.find('h1', {'class': 'ng-binding'}).text, 'nextDepart': stopData.find('div', {'class': 'stop-timing'}).find('strong').text})

for stop in stopsData :
  print(stop.stopName + '... Next departure in: ' + stop.nextDepart)

#line13url = "https://nxbus.co.uk/coventry/information/buses-to-from/services-in-coventry"
#page = urlopen(line13url)
#soup = BeautifulSoup(page, 'html.parser')
#bus_stop1 = soup.find('a', {'class': "13"}).text
#routeTo = soup.find('td', {'class': 'main_and_via'})
#destination = routeTo.find('a').text
#via = routeTo.find('span', {'class': 'via'}).text
#via = via[3:len(via)]
#via = via[0:4] + ':' + via[4:len(via)]

#print("Route number: " + bus_line, "  Destination: ")# + destination, via)
