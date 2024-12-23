
from enum import Enum
import os
import platform
import json
from colorama import Fore, Back, Style, init

init(autoreset=True)
cars = []
FILENAME = "myGarage"
class Actions(Enum):
    ADD = 1
    DELETE = 2
    DISPLAY = 3
    FIND = 4
    EXIT = 5

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    try:
        for act in Actions:
            print(f"{act.value}-{act.name}")
        
        user_selection = int(input("Please select an option: "))
        if 1 <= user_selection <= len(Actions):
            return Actions(user_selection)
        else:
            print(Fore.BLACK + Back.RED + "Invalid option")

    except ValueError:
        print(Fore.BLACK + Back.RED + "invalid!, Please select a valid index from the list!")
    
def addCar():
    cars.append({
        "brand" : input("Brand: "),
        "model" : input("Model: "),
        "color" : input("color: "),

    })

    displayCars()
    saveGarage()

def deleteCar():
    displayCars()
    try:
        carToDelete = int(input("Select a car to delete: (index)"))
        if cars[carToDelete] in cars:
            print(f"Car: {cars[carToDelete]['brand']},{cars[carToDelete]['model']},{cars[carToDelete]['color']} has been deleted! ")
            cars.pop(carToDelete)
            displayCars()
            saveGarage()
        else:
            print(Fore.BLACK + Back.RED + f"Car '{carToDelete}' was not found!")
    except ValueError:
        print(Fore.BLACK + Back.RED + "invalid!, Please select a valid index from the list!")
    except IndexError:
        print(Fore.BLACK + Back.RED + "Car was not found!")
    
def displayCars():

    print(Fore.WHITE + Back.CYAN + Style.BRIGHT + "Your Cars:")
    
    for index, car in enumerate(cars):
        print(Fore.BLACK + Back.GREEN + f"{(index)}: {car['brand']},{car['model']},{car['color']} ")

def findCar():
    try:
        carToFind = int(input("Select a car to find: (index)"))
        if cars[carToFind] in cars:
            print(Fore.BLACK + Back.GREEN + f"Found car: {cars[carToFind]['brand']},{cars[carToFind]['model']},{cars[carToFind]['color']}")
                
    except ValueError:
        print(Fore.BLACK + Back.RED + "invalid!, Please select a valid index from the list!")
    except IndexError:
        print(Fore.BLACK + Back.RED + "Car was not found!")

def saveGarage():
    with open(FILENAME, 'w+')as f:
        json.dump(cars, f, indent=4)
            
    f.close()

def loadGarage():
    global cars
    try:
        with open(FILENAME, 'r')as f:
            cars = json.load(f)
    except FileNotFoundError:
        print(Fore.BLACK + Back.RED + "File was not found!")


if __name__ == "__main__":

    while True:
    
        print("Welcome to my garage!")
        loadGarage()
        user_selection = menu()
        # clear_terminal()
        if user_selection == Actions.ADD:
            addCar()
        elif user_selection == Actions.DELETE:
            deleteCar()
        elif user_selection == Actions.DISPLAY:
            displayCars()
        elif user_selection == Actions.FIND:
            findCar()
        elif user_selection == Actions.EXIT:
            print("Goodbye!")
            exit()
            
        
    
    