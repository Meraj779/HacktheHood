checklist = []

def create(item):

    checklist.append(item)

    return "Added {} to checklist".format(item)

def read(index):

    print(checklist[index])

    return checklist

def update(index, item):

    old = checklist[index]

    checklist[index] =item

    return "Changed {} to {}".format(old, item)

def destroy(index):

    removed = checklist[index]

    checklist.pop(index)

    return "Removed {} from checklist".format(removed)

def all_items():

    item = []
    
    for el in checklist:
        print(el)
        item.append(el)

def checklist(index):

    unchecked = checklist[index]

    checklist[index] = ", " + unchecked

    return checklist[index]

def user_input(prompt):

    entry = input(prompt)

    return entry

def user_choice():

    editing = True

    while editing:

        choice = user_input("Which function would you like to use? Enter C for create, & for read, U for update and 0 for destroy. ")

        if choice == "C" or choice == "c":

            item = user_input("What item do you wish to create? Type out the memo of your desired item. ")
            
            create(item)

            continue

        elif choice == "A" or choice =="r":

            index = user_input("What item do you wish to read? Give a number for the position of the item. ")

            read(int(index))

            continue

        elif choice == "U" or choice == "u":

            update_index = user_input("What item do you wish to update?. Please give a number for the positio of the item. ")
            
            new_item = user_input["Type out the name of your new  item"]
            
            update(int(update_index), new_item)

            continue

        elif choice == "D" or choice == "d":

            delete_index = user_input("What item do you wish to update?. Please give a number for the positio of the item. ")
            
            destroy(delete_index)

            continue

        else:

            end = user_input("Do you want to quit? Enter Y for Yes or N for no. ")

            if end == "Y" or end == "y":
                print(checklist)
                editing = False

            else:

                continue

def test():

    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    print(read(0))
    print(all_items()
    print(checked(0))
    print(user_input("Is this working? "))
    user_choice[]

while editing:
    user_choice()

user_choice