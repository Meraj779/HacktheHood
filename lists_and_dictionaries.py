dict_food={"Chicken": 1.59, "beef": 1.99, "Cheese" : 1.00, "Milk": 2.00}
print(dict_food)
NBA_players={"Stephen Curry": 30, "Michael Jordan": 23, "James Harden": 13, "Kobe Bryant": 24}
print(NBA_players)

Steph_jersey=NBA_players["Stephen Curry"]

print(Steph_jersey)

chicken_price = dict_food["Chicken"]

print(chicken_price)

NBA_players["Michael Jordan"]= -17

print(NBA_players)

shoe_price={"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

print(shoe_price)

shoe_price["SB Dunk"] -=2

print(shoe_price)

shoe_price["Yeezy"] -=1

print(shoe_price)

shoe_price["Jordan 13"] +=7

print(shoe_price)

shoe_price["Yeezy"] +=7

print(shoe_price)

shoe_price["Foamposite"] +=7

print(shoe_price)

shoe_price["Air Max"] +=7

print(shoe_price)

shoe_price["SB Dunk"] +=7

print(shoe_price)

shoe_price["Jordan 13"] -=3

print(shoe_price)

shoe_price["Yeezy"] -=3

print(shoe_price)

shoe_price["Foamposite"] -=3

print(shoe_price)

shoe_price["Air Max"] -=3

print(shoe_price)

shoe_price["SB Dunk"] -=3

print(shoe_price)

NBA_players["Luka Doncic"] = 77

print(NBA_players)

del NBA_players["Michael Jordan"]

print(NBA_players)

def total_price(food_items, food_items2):
    total=dict_food[food_items]+dict_food[food_items2]
    return total

def price_diff(food_items, food_items2):
    diff=dict_food[food_items]-dict_food[food_items2]
    return abs(diff)

def shoe_restock(shoe, num):
    shoe_price[shoe] *=num
    return shoe_price 

def clearance_sale(shoe, num):
    shoe_price[shoe] /=num
    return shoe_price 

def supply_search(dict):
    largest=0
    supply=''

    for key in dict.keys():
        if dict[key] > largest:
            largest=dict[key]
            supply=key

    return (supply, largest)

print(total_price("beef", "Chicken"))
print(price_diff("beef", "Chicken"))
print(shoe_restock("Yeezy", 3))
print(clearance_sale("SB Dunk", 5))
print(supply_search(NBA_players))