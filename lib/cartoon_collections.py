

def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        index = dwarves.index(dwarf)
        print(f"{index + 1}. {dwarf}")

def summon_captain_planet(calls):
    newList = []
    for call in calls:
        capitalCall = call.capitalize()
        newList.append(capitalCall + "!")
    return(newList)

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
        cheeses = {"cheddar", "gouda", "camembert"}
        for snack in snacks:
            if snack in cheeses:
                return snack
        else:
            return None

dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

roll_call_dwarves(dwarves)
summon_captain_planet(planeteer_calls)
