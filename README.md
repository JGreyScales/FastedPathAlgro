# FastestPathAlgro

Calculates the fastest path through a randomly generated series of walkpaths, buses, and trains- times for each is pre-determined. Comments in code explain the math for random generation and times

possibleStations = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

station amount is a random interger between 4 and 12
#amount of footpaths = stations / 4
#walking takes twice as long as the train

#amount of busPaths = footpaths - 1 if the amount of terminals is not divisible by 3
#otherwise busPaths = footpaths

#movement directyl to the left letter is always allowed, costing 1 hour
