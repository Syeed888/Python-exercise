def get_options():
    return input("Enter command: ")

def create_new_station(stations):
    print("Creating a new station..")
    code = input("Enter ICAO code: ")
    name = input("Enter name: ")
    stations[code] = name

def fetch_station(stations):
    print("Fetching station..")
    search_term = input("Enter ICAO code: ")
    if search_term not in stations:
        print(f"No station found with ICAO code {search_term}.")
    else:
        print(f"Station found with ICAO code {search_term}: {stations[search_term]}")

def program(command, stations):
    if command == "new":
        create_new_station(stations)
    elif command == "fetch":
        fetch_station(stations)
    else:
        print("Unknown command")

command = get_options()
stations = {}
while command != "quit":
    program(command, stations)
    command = get_options()
print("bye")