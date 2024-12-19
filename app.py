from icecream import ic
from enum import Enum
import ast
import os
import platform


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
    for act in Actions:
        print(f"{act.value}-{act.name}")
    return int(input("Please select an option: "))

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
    carToDelete = int(input("Select a car to delete: (index)"))

    print(f"Car: {cars[carToDelete]['brand']},{cars[carToDelete]['model']},{cars[carToDelete]['color']} has been deleted! ")

    cars.pop(carToDelete)
    displayCars()
    saveGarage()
  
    
def displayCars():

    ic(("Your Cars:"))
    
    for index, car in enumerate(cars):
        print(f"{(index)}: {car['brand']},{car['model']},{car['color']} ")

def findCar():
    
    carToFind = int(input("Select a car to find: (index)"))
   
    print(f"Found car: {cars[carToFind]['brand']},{cars[carToFind]['model']},{cars[carToFind]['color']}")

def saveGarage():
    with open(FILENAME, 'w+')as f:
        f.write(str(cars))
            
    f.close()

def loadGarage():
    global cars
    try:
        with open(FILENAME, 'r')as f:
            cars = ast.literal_eval(f.read())
    except FileNotFoundError:
        print("File was not found!")


if __name__ == "__main__":

    while True:
    
        print("Welcome to my garage!")
        loadGarage()
        user_selection = Actions(menu()) #why use class "Actions"
        clear_terminal()
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
            
        
    
    