import time
import sys
import os

check_file = "bank.txt"
if os.path.isfile(check_file):
    print(f""""Existing Save File Detected '{check_file}'... 

Would you like to OPEN or create NEW save file?""")
    choice = input('>')

    if choice.lower() == "open":
        print("Saved Bank Opened")
        input_file_1 = open(check_file, 'r+')

    elif choice.lower() == "new":
        print("This will delete your old save, are you sure ? Y/N")
        choice_2 = input('>')

        if choice_2.lower() == 'y':
            input_file_1 = open(check_file, 'w+')
            input_file_1.write('0')
            input_file_1.close()

        elif choice_2.lower() == 'n':
            sys.exit('We must say goodbye to the past before we can look to the future...')

        else:
            sys.exit('Input Not Accepted')


else:
    input_file_1 = open('bank.txt', 'w+')
    print("New Bank Save Created")

inventory = []

global wallet

global beach_red_rock
global beach_grey_rock
global beach_white_rock
global mountain_black_rock

wallet = 0

beach_red_rock = 5
beach_grey_rock = 5
beach_white_rock = 1
mountain_black_rock = 8


def username_enter():
    print("""Hey, and welcome to 'Rock'star 6.
Here you can buy and sell all your favourite rocks, from the safety of your own home.""")

    time.sleep(1)
    print("Please enter your username")

    username = input("> ")
    print(f"Hey {username} ! Lets play !")
    print("""
    At any time you can type, INVENTORY, BANK or WALLET to check their stats
    
    All possible commands are highlighted as CAPITAL
    
    Press Enter to Continue !
    """)

    input("ENTER")

    time.sleep(1)
    print("""You step off the boat with the sun on your face and adventure in your heart.
    It has been a dream since childhood to come to The Kingdom of Simon and engage in Rockstrophy of the 
    highest order. """)
    time.sleep(2)
    start()


def beach():
    global beach_red_rock
    global beach_grey_rock
    global beach_white_rock

    while True:
        time.sleep(1)
        print("You are on a warm sunny beach, you think you can see some rocks of interest...")
        time.sleep(2)
        print("Would you like to SEARCH for rocks or go BACK to the crossroads?")
        choice_direction = input("> ")

        if choice_direction.lower() == "search":
            break

        elif choice_direction.lower() == "back":
            start()

        elif choice_direction.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice_direction, wallet, inventory, input_file_1)

        else:
            print("I don't understand...")

    print(f"""Searching on the floor you see {beach_red_rock} red rocks, 
{beach_grey_rock} grey rocks and a {beach_white_rock} white rock!""")

    while True:
        print("Which rock should you pick up? Or BACK to return")
        print("RED, GREY, WHITE")
        print(f"Red Rocks: {beach_red_rock} Grey Rocks: {beach_grey_rock} White Rocks: {beach_white_rock}")
        rock_choice = input("> ")

        if rock_choice.lower() == "back":
            beach()

        if rock_choice.lower() == "red":

            if beach_red_rock >= 1:
                print("You picked up a red rock!")
                inventory.append("Red Rock")
                beach_red_rock -= 1

            elif beach_red_rock == 0:
                print("There are no red rocks to collect...")

        elif rock_choice.lower() == "grey":

            if beach_grey_rock >= 1:
                print("You picked up a grey rock!")
                inventory.append("Grey Rock")
                beach_grey_rock -= 1

            elif beach_grey_rock == 0:
                print("There are no grey rocks to collect... ")

        elif rock_choice.lower() == "white":

            if beach_white_rock >= 1:
                print("You picked up a white rock!")
                inventory.append("White Rock")
                beach_white_rock -= 1

            elif beach_white_rock == 0:
                print("There are no white rocks to collect... ")

        elif rock_choice.lower() == "bank" or "wallet" or "inventory":
            statcheck(rock_choice, wallet, inventory, input_file_1)

        else:
            break


def mountains():
    global mountain_black_rock

    time.sleep(3)
    print("You reach the saddle of two tall mountains, you think you can see some interesting rocks...")
    time.sleep(1)
    while True:
        print("Would you like to SEARCH for rocks or go BACK to crossroads?")
        choice_direction = input('>')
        if choice_direction.lower() == "search":
            break

        elif 'back' in choice_direction.lower():
            start()

        elif choice_direction.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice_direction, wallet, inventory, input_file_1)

        else:
            print(f"Sorry i cant {choice_direction} right now...")
            time.sleep(0.5)

    print("You look around on the ground and see some rocks... its getting dark though we should be quick...")
    print(f"You see {mountain_black_rock} black mountain rocks...  Should we take them quickly?.. Y/N")

    while True:
        count = 0
        choice_rock = input(">")

        if "y" in choice_rock.lower():
            for x in range(mountain_black_rock + 1):

                if x > 0:
                    count += 1
                    print(f"{count}")
                    inventory.append("Black Rock")
                    mountain_black_rock -= 1
                    time.sleep(0.2)

            print(f"That's it.. there are {mountain_black_rock} left...")
            print(f"you have {inventory} in your inventory.")
            print("Enter to return")

        elif "n" or "back" in choice_rock.lower():
            mountains()

        elif choice_rock.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice_rock, wallet, inventory, input_file_1)

        else:
            print(f"I don't get what {choice_rock} is supposed to be to me?")


def river():
    time.sleep(0.5)
    print("""You can hear the rushing of the water as you step through a clearing in the trees...
You can see some interesting rocks on the shore...""")
    time.sleep(5)
    print("""
    
Oh fuck its the troll under the bridge, Racist Barry...
    
You try to rub his belly with fresh cinnamon 
    
"No wishes for you today !" He Cries
    
Quick back to the crossroads !    
    """)
    time.sleep(8)
    start()


def city_centre():
    time.sleep(0.5)
    print("The hustle and bustle of the city continues around you... You see a BAKERY, PAWN SHOP and a BANK.")
    choice = input("> ")

    if choice.lower() == "bank":
        bank()

    elif choice.lower() == "pawn shop":
        pawn_shop()

    elif choice.lower() == "bakery":
        bakery()

    elif choice.lower() == "bank" or "wallet" or "inventory":
        statcheck(choice, wallet, inventory, input_file_1)

    elif choice.lower() == "back" or "leave" or "start":
        start()

    else:
        city_centre()


def bank():
    global wallet

    while True:
        print("Welcome to the bank, would you like to DEPOSIT or WITHDRAW or go BACK?")
        choice = input("> ")

        if choice.lower() == "deposit":
            bank_deposit(wallet)

        elif choice.lower() == "withdraw":
            bank_withdraw()

        elif choice.lower() == 'back' or 'city' or 'city centre':
            city_centre()

        elif choice.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice, wallet, inventory, input_file_1)

        else:
            print("I'm sorry i don't understand that...")


def bank_deposit(wallet):
    while True:
        print(f"You have {wallet} in your wallet, how much would you like to deposit? Press ENTER to leave")
        deposit = input("> ")
        if deposit.isnumeric():

            deposit_int = int(deposit)

            if wallet - deposit_int < 0:
                print("Im sorry, you don't have enough funds...")

            elif wallet - deposit_int >= 0:
                with open(input_file_1, 'r') as current_bank:
                    contents = current_bank.read()

                new_balance = int(contents) + deposit_int
                converted_new_balance = str(new_balance)

                wallet -= deposit_int

                open(input_file_1, 'w').write(converted_new_balance)
                print(f"Thank you for depositing {deposit} gold or silver or whatever.")

                return wallet

            else:
                break
        else:
            break


def bank_withdraw():
    global wallet

    while True:
        with open(input_file_1, 'r') as current_bank:
            contents = current_bank.read()

        print(f"You have {contents} in your bank, how much would you like to withdraw?")
        withdraw = input("> ")
        if withdraw.isnumeric():

            withdraw_int = int(withdraw)
            contents_int = int(contents)
            if contents_int - withdraw_int < 0:
                print("Im sorry, you don't have enough funds...")

            elif contents_int - withdraw_int >= 0:
                new_balance = contents_int - withdraw_int
                converted_new_balance = str(new_balance)

                wallet += withdraw_int

                open(input_file_1, 'w').write(converted_new_balance)
                print(f"Thank you for withdrawing {withdraw} gold or silver or whatever."
                      f"You have {wallet} in your wallet")

                return wallet

            else:
                break
        else:
            break


def pawn_shop():
    print(
        "You enter the shop, there are rocks all over the shelves and in display cabinets. It has that old rock smell")
    while True:
        print("Would you like to SELL rocks or go BACK ?")
        choice = input("> ")

        if "sell" in choice.lower():
            pawn_shop_sell()

        elif "leave" or "back" in choice.lower():
            city_centre()

        elif choice.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice, wallet, inventory, input_file_1)

        else:
            print("I'm sorry, i don't understand that...")


def pawn_shop_sell():
    while True:

        global wallet

        print("What would you like to sell ? ")
        print(f"Inventory: {inventory}. Wallet: {wallet}")
        choice = input("> ")
        choice_t = choice.title()

        if choice_t in inventory:
            inventory.remove(choice_t)

            if choice_t == "Red Rock":
                wallet += 1
                print("You have sold a red rock for 1 rusty coin")
                time.sleep(1)

            elif choice_t == "Grey Rock":
                wallet += 1
                print("You have sold a red rock for 1 fresh'ish' cucumber")
                time.sleep(1)

            elif choice_t == "White Rock":
                wallet += 5
                print("You have sold a white rock for 5 golden rings")
                time.sleep(1)

            elif choice_t == "Black Rock":
                wallet += 0.5
                print("You have sold a black rock for 50p of pick n mix")

            else:
                print(f"Sorry you cant sell {choice}")

        elif choice == "back" or "leave":
            pawn_shop()

        elif choice.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice, wallet, inventory, input_file_1)

        elif choice not in inventory:
            print(f"Sorry you don't appear to have any {choice} in your bag ")

        else:
            break


def bakery():
    global wallet

    print("You smell fresh bread and rat poison. Your stomach begins to rumble...")

    while True:
        time.sleep(1.5)
        print("Would you like to BUY bread or LEAVE ?")
        choice = input("> ")

        if choice.lower() == "buy":
            bakery_buy(wallet)

        elif choice.lower() == "leave" or "back":
            city_centre()

        elif choice.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice, wallet, inventory, input_file_1)

        else:
            print("Sorry I don't understand that ...")


def bakery_buy(wallet):
    loaf = 3
    cake = 5
    cigarettes = 2

    while True:
        print("What would you like to buy?")
        print(f"{loaf} loafs of BREAD (£1), {cake} CAKEs (£2) and {cigarettes} packs of CIGARETTES (£10).")
        print(inventory)
        print(wallet)
        choice = input("> ")

        if choice.lower() == "bread":

            if loaf > 0 and wallet >= 1:
                print("You have bought a loaf of bread")
                inventory.append("Loaf of Bread")
                loaf -= 1
                wallet -= 1

            elif loaf == 0 or wallet == 0:
                print("We are out of stock of bread right now.. or you cant afford it... pick one! !")

        elif choice.lower() == "cake":

            if cake > 0 and wallet >= 1:
                print("You have bought a cake !")
                inventory.append("Cake")
                cake -= 1
                wallet -= 1

            elif cake == 0 or wallet == 0:
                print("We are out of stock of cakes right now or you cant afford it... pick one! !")

        elif choice.lower() == "cigarettes":
            if cigarettes > 0 and wallet >= 20:
                time.sleep(1)
                print("The baker stares at you for a moment..")
                time.sleep(3)
                print("You dirty cunt.. have your filthy fags!")
                time.sleep(1)
                print("He throws them at you and they land on the floor... you quickly grab them as he chases you out")
                time.sleep(4)
                print("As you reach the door he has jumped over the counter"
                      "\n As you step out to freedom he smashes your dirty cunt face in with a rolling pin....")
                time.sleep(5)
                print(".... just like mama used to...")
                time.sleep(1)
                print("You drift into unconsciousness as you climax for the first time since her funeral... ")
                wallet -= 20
                end_credits()

            elif cigarettes == 0:
                break

        elif choice.lower() == "bank" or "wallet" or "inventory":
            statcheck(choice, wallet, inventory, input_file_1)

        elif "leave" or "back" in choice.lower():
            bakery()

        else:
            print("Sorry i don't understand that...")


def end_credits():
    time.sleep(3)
    print("Thanks for playing 'Rock'Star, you really are a rockstar!")
    time.sleep(1)
    exit(0)


def start():
    print("""You see a signpost, it reads: 
    BEACH 1km
    MOUNTAINS 3km
    RIVER 500m
    CITY CENTRE""")

    print("In your bag you have:")
    print(inventory)

    while True:
        print("Where would you like to go?")
        choice = input("> ")
        if "bank" or "wallet" or "inventory" in choice.lower():
            statcheck(choice, wallet, inventory, input_file_1)

        if choice.lower() == "beach":
            beach()

        elif choice.lower() == "mountains":
            mountains()

        elif choice.lower() == "river":
            river()

        elif choice.lower() == "city centre":
            city_centre()


def statcheck(inp, w, i, bank_file):
    print(inp)
    if inp == "wallet":
        print(w)
        time.sleep(2)

    elif inp == "inventory":
        print(f"You have {len(inventory)} items in inventory")
        print_inventory(inventory)


    elif inp == "bank":
        print(input_file_1.read())
        input_file_1.close()


def print_inventory(inventory):
    sorted_i = sorted(inventory)
    print(sorted_i)


username_enter()
