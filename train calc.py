import random


# randomizes the amount of stations that will exist
possibleStations = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
stations = []
footpaths = []
busPaths = []
for x in range(random.randint(4, len(possibleStations))):
    stations.append(possibleStations[x])


placeholder = stations.copy()


# randomizes the footpaths that exist between terminals
# amount of footpaths = stations / 4


# walking takes twice as long as the train

while len(placeholder) / 4 >= 1:
    while 1:
        stationOne = random.choice(placeholder)
        stationTwo = random.choice(placeholder)
        if stationOne != stationTwo:
            footpaths.append( (stationOne, stationTwo) )
            placeholder.remove(stationOne)
            placeholder.remove(stationTwo)
            break



placeholder = stations.copy()

# randomizes the bus paths that exist between terminals 
# amount of busPaths = footpaths - 1 if the amount of terminals is not divisible by 3
# otherwise busPaths = footpaths

# busing takes 1.5 times longer than the train
while len(placeholder) / 5 > 1:
    while 1:
        stationOne = random.choice(placeholder)
        stationTwo = random.choice(placeholder)
        if stationOne != stationTwo:
            busPaths.append( (stationOne, stationTwo) )
            placeholder.remove(stationOne)
            placeholder.remove(stationTwo)
            break

print(f"Stations:{stations}\nBuspaths:{busPaths}\nFootPaths:{footpaths}\n")






def waveCollapse(path, allRoutes : list, depth, goal):
    possibleRoutes = []

    if len(path) >= len(allRoutes[0]) + 1:
        return (13, [])
    if path[-1] == goal[0]:
        return (depth, path)

    currentPosition = allRoutes[0].index(path[-1:][0])
    

    try:
        if currentPosition != 0:
            possibleRoutes.append( (("", allRoutes[0][currentPosition - 1]), 1) )
    except: pass
    try:
        if currentPosition != len(allRoutes[0]) - 1:
            possibleRoutes.append( (("", allRoutes[0][currentPosition + 1]), 1) )
    except: pass

    for x in range(1,3,1):
        if x == 1: y = 1.5
        for route in allRoutes[x]:
            for station in range(2):
                if route[station] == path[-1]:
                    possibleRoutes.append( (route, y) if station == 0 else (route[::-1], y))

    # removes any paths that will loop back onto a previous path
    for route in possibleRoutes:
        try:
            path.index(route[0][1])
            possibleRoutes.remove(route)
        except (ValueError):
            pass

    acceptedAnswers = []
    for route in possibleRoutes:
        currentPath = path.copy()
        currentPath.append(route[0][1])
        returnedDepth = waveCollapse(currentPath, allRoutes, depth + route[1], goal)
        if returnedDepth != None: acceptedAnswers.append(returnedDepth)
    return acceptedAnswers

# current stations, all routes, depth
allRoutes = waveCollapse(["A"], [stations, busPaths if len(busPaths) > 0 else "", footpaths], 0, stations[-1:])

def searchResults(route: list, fastestRoute):
    for subRoute in route:
        if type(subRoute) == tuple:
            if subRoute[0] < fastestRoute[0]:
                fastestRoute = subRoute
        elif type(subRoute) == list: 
            fastestRoute = searchResults(subRoute, fastestRoute)
    return fastestRoute

fastestRoute = (13, [])
for route in allRoutes:
    fastestRoute = searchResults(route, fastestRoute)

print(f"The fasted route will take: {fastestRoute[0]}hrs and its the path of {fastestRoute[1]}")