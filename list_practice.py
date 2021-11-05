dict_city=[]

print(dict_city)

world_city=["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]

print(world_city)

country=["California", "Canada", "China", "Texas", "Arizona", "London", "France", "Alaska", "Hawaii", "Scotland"]

print(country)

print(world_city[0], world_city[4], world_city[5])

four_cities=world_city[0:4]

print(four_cities)

world_city[0]="San Francisco"

world_city[2]="Brooklyn"

world_city[-3]="Hollywood"

world_city[-5]="Tampa"

print(world_city)

world_city.append("Oakland")

world_city.extend(["New York City", "Los Angeles"])

world_city.insert(0, "Miami")

print(world_city)

del world_city[1]

world_city.pop(-3)

world_city.remove("Los Angeles")

print(world_city)

def print_city(list):
    for el in list:
        print(el)
    return "All the cities are there in the list"

def reorganize_list(list):
    # [1, 2, 3, 4, 5]
    print(list)
    counter=0

    while counter < len(list):
        item1= list[counter]
        item2= list[counter +1]

        if len(item1) >= len(item2):
            counter += 1
            continue
        elif counter +1 == len(list) -1:
            break
        else:
            list.remove(item1)
            list.append(item1)
            counter += 1
    return list

print(print_city(world_city))
print(reorganize_list(world_city))