which_line = input("Which bus line would you like to know? ")

try:
    print("Here is the current expected departure time at bus stop " + bus_stop + " for bus line " +
        resp['departures'][which_line][0]['line_name'] + " heading to " + resp['departures'][which_line][0]['direction'])
    print("Expected departure time: " +
        resp['departures'][which_line][0]['expected_departure_time'])
    print("The next bus at bus stop " + bus_stop + "," + " for bus line " +
        resp['departures'][which_line][1]['line_name'] + " will be heading to " + resp['departures'][which_line][1]['direction'])
except KeyError as err:
    print("%s is not a valid line: %s" % (which_line, err))
