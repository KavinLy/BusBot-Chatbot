from urllib.request import urlopen
import json 

def askbot(bus_stop):

    if bus_stop == "CU2":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43001053801/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CU1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000006201/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "MP1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43009012501/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "SJ1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43009012601/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BY4":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000002103/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "WR1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000008201/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "WR3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000008203/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BY1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000002101/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "LP1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000007201/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "ES1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000007102/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CU5":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43001053502/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "FX1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000006301/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "TS3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001003/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BS6":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001202/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CS3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000003203/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "VR2":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43001006502/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "GR2":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000008302/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BS5":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001203/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CS1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000003201/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CR4":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000009104/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "VR3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43001006501/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CS4":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000003206/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BS3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000003102/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "UL3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000004104/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CR2":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000009102/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CS2":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000003202/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CU4":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43001053702/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "TS5":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43001054401/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "ER4":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000008105/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "ER1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000008101/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "GR1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000008301/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CU3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43001054201/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BS4":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001204/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "UL1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000004106/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "UL4":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000004101/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "HS1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001101/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "TS4":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001004/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "TS1":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001001/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BY5":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000002104/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "HS3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43001025501/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "TS2":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001002/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "HS2":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000001102/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "CR3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000009103/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BY3":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000002105/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    elif bus_stop == "BY2":
        url = urlopen("https://transportapi.com/v3/uk/bus/stop/43000002102/live.json?app_id=cac11064&app_key=dde28481a2aadc583d6425adc379637e&group=route&nextbuses=yes")
        departures(url, bus_stop)
    else:
        print("That bus stop is not on my list! Try another")

def departures(url, bus_stop):
    data = json.loads(url.read().decode())
    json_str=json.dumps(data)
    resp=json.loads(json_str)  
    which_line = input("Which bus line would you like to know? ")
    try:
        print("Here is the current expected departure time at bus stop " + bus_stop + " for bus line " + resp['departures'][which_line][0]['line_name'] + " heading to " + resp['departures'][which_line][0]['direction'])
        print("Expected departure time: " + resp['departures'][which_line][0]['expected_departure_time'])
        print("The next bus at bus stop " + bus_stop + "," + " for bus line " + resp['departures'][which_line][1]['line_name'] + " will be heading to " + resp['departures'][which_line][1]['direction'])
    except KeyError:
        print("Line " + which_line + " is not a valid line or is not expected to arrive currently at the bus stop: " + bus_stop)
    except IndexError:
        print("This is currently the latest departure for line: " + which_line)

which_stop = input("Which bus stop timetable would you like to know? ")
stop = which_stop.upper()
askbot(stop)
