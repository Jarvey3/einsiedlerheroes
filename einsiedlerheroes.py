
import pyfiglet
import sys
from datetime import datetime

hero_names = ["ein siedler", "Noudle", "Bhutan Flag", "Vegan Chicken Nuggets"]
# prices of heroes in the shop
hero_prices = [0, 100, 200, 20]


# collection of heroes owned. Syntax [heroID,heroLevel,heroExp]
heroes = [[0, 1,0]]
# TODO implement heroExp System

# global vars
money = 100


# TODO Implement level and Exp System. These don't provide any use yet
level = 1 
level_exp = 0
total_exp = 0
exp_per_level = [100,200,500]


def getStats(heroID, level):
    """Returns stats of hero with respective id and level
    """
    # TODO Create balanced stats for each character
    # TODO #1 Move stats in an external file
    # ein siedler
    einsiedler_off = 5, 10, 15, 20, 25, 30
    einsiedler_def = 20, 25, 30, 35, 45, 50
    einsiedler_hea = 30, 40, 50, 60, 70, 80
    # Noudle
    noudle_off = 30, 40, 50, 60, 70, 80
    noudle_def = 20, 25, 30, 35, 40, 45
    noudle_hea = 50, 60, 70, 80, 90, 100
    # TODO other stats
    match heroID:
        case 0:
            return(einsiedler_off[level], einsiedler_def[level], einsiedler_hea[level])
        case 1:
            return(noudle_off[level], noudle_def[level], noudle_hea[level])


def init():
    # TODO restore player progress
    welcomeBanner = pyfiglet.figlet_format("Ein Siedler Heroes")
    print(welcomeBanner)
    print("The official ein siedler hero fighter and collector")
    print("\nVersion 1.0")
    print("created by @ein siedler")
    main()


def main():
    """Handle user input
    """
    while True:
        
        print("What would you like to do?")
        cmd = input().upper()
        match cmd:
            case "B":
                # go to battle menu
                battleMenu()
            case "C":
                # display card collection
                displayCollection()
            case "H":
                # display help
                help()
            case "Q":
                # quit
                quit()
            case "S":
                # display shop
                shop()
            case _:
                print("This feature is currently not supported")
        print(pyfiglet.figlet_format("Hub"))


def battleMenu():
    """Displays the battle menu
    """
    # TODO implement BattleMenu
    print(pyfiglet.figlet_format("Battles"))
    print("Do you want to battle?")
    if(yesNo()):
        hero = selectHero()
        battle(hero)
    
def selectHero():
    """prompts the user to choose a hero to fight with
    """
    # TODO implement hero selection
    pass


def battle(heroId):
    """performs a battle with the given hero
    """
    # TODO implement battle
    pass

def displayCollection():
    """Displays the users card collection
    """
    # TODO implement displaying of collection
    print(pyfiglet.figlet_format("Collection"))
    global heroes
    for hero in heroes:
        id = hero[0]
        off, deff, health = getStats(id, hero[1])
        printHeroStats(id, off, deff, health, hero[2])
        print("")


def help():
    """Prints help for user actions
    """
    try:
        f = open("help.txt", "r")
        print("\n" + f.read())
    except:
        print(
            "\nNo helpfile found. Please download all provided files for full functionality")


def quit():
    """save and end game
    """
    # TODO implement saving
    print(pyfiglet.figlet_format("Goodbye"))
    sys.exit()


def shop():
    """Buy new cards
    """
    # TODO implement shop
    print(pyfiglet.figlet_format("Shop"))
    print("Your money: " + str(money))
    print("\n---OFFERS---")
    offers = getOffers()
    for offer in offers:
        showShopEntry(offer)
        print("")
    print("Enter ID of the hero you want to buy. Press Q to quit")
    while buyDialog(offers) == False:
        print("Enter ID of the hero you want to buy. Press Q to quit")


def buyDialog(offers):
    """Dialog for buying a certain hero from the shop"""
    # TODO handle wrong ids
    id = input()
    if id.upper() == "Q":
        print("See you next time")
        return True
    id = int(id)
    for offer in offers:
        if id == offer:
            return buy(offer)
    return False


def buy(id):
    """Buy a hero
    """
    global money
    global hero_prices
    global heroes
    global hero_names
    if(money - hero_prices[id] < 0):
        print("You can't afford this hero")
        return False
    else:
        money -= hero_prices[id]
        heroes.append([id, 1,0])
        print("Succesfully bought " + hero_names[id])
        return True

# ---Section---

# helpers

def yesNo():
    """reads for a yes/no from console
    """
    while True:
        res = input()
        if(res == "y" or res == "Y"):
            return True
        if(res == "n" or res == "N"):
            return False
        print("Please provide a valid anser [Y/N]")


def getOffers():
    """Returns offers for the current day of the week
    """
    # TODO finish offers
    day = datetime.today().weekday()
    match day:
        case 0:
            defaultOffers = 1, 2, 3
            return getUnowned(defaultOffers)
        case 1:
            defaultOffers = 1, 2, 3
            return getUnowned(defaultOffers)
        case 2:
            defaultOffers = 1, 2, 3
            return getUnowned(defaultOffers)
        case 3:
            defaultOffers = 1, 2, 3
            return getUnowned(defaultOffers)
        case 4:
            defaultOffers = 1, 2, 3
            return getUnowned(defaultOffers)
        case 5:
            defaultOffers = 1, 2, 3
            return getUnowned(defaultOffers)
        case 6:
            defaultOffers = 1, 2, 3
            return getUnowned(defaultOffers)


def showShopEntry(id):
    """Prints the shop entry for a given hero id
    """
    global hero_prices
    global hero_names
    print(hero_names[id] + "\nLevel 1\tPrice " +
          str(hero_prices[id]) + "\tID " + str(id))


def getUnowned(defaultHeroes):
    """Returns only the unowned heroes from a list of given heroes
    """
    ResultList = []
    for hero in defaultHeroes:
        if(not checkIfOwned(hero)):
            ResultList.append(hero)
    return ResultList


def checkIfOwned(id):
    """Checks whether a hero with the given id is already owned by the player. Returns true if owned
    """
    global heroes
    for hero in heroes:
        if hero[0] == id:
            return True
    return False


def printHeroStats(id, off, deff, health,exp):
    """Print Name and current values of hero"""
    print(hero_names[id] + "\nOffense " + str(off) +
          "\tDefense " + str(deff) + "\tHealth " + str(health) + "\tExp " + str(exp))


if __name__ == "__main__":
    init()
