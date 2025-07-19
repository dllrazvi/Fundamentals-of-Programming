import random

import functions
def printall(flight:list,code:int,depcity:str,destcity:str,duration:int):
    for i in range(len(flight)):
        print("Airplane ",code[i]," departs from ",depcity[i]," with the destination ",destcity[i]," and duration ",duration[i])
def random_generator(code:int):
    char=["0","1","2","3","4","5","A","B","C"]
    code=random.choice(char)

def user_interface():
    cityd= ["Baia Mare","Cluj Napoca","Brasov","Iasi","Zalau"]
    cityde= ["Londra","Paris","Manchester","Zurich","Munchen"]
    flight= []
    for i in range(len(flight)):
        depcity=random.choice(cityd)
        destcity=random.choice(cityde)
        code=random_generator()
        duration=random.randint(20,100)
        functions.add_newf(code,duration,depcity,destcity,flight)

    print("What option do you choose?")
    print("Add - add a flight")
    print("Delete- delete a flight")
    print("Show - show all flights with a given departure city")
    option=input("The option chosen: ")
    if option=="Add":
        code=input("Code: ")
        depcity = input("Departure city: ")
        destcity=input("Destination city: ")
        duration=input("Duration of the flight: ")
        functions.add_newf(code,duration,depcity,destcity,flight)
    elif option=="Delete":
        code=input("The flight code: ")
        functions.delete_flight(code,flight)
    elif option=="Show":
        functions.citysort(flight,destcity)
        printall(flight,code,depcity,destcity,duration)
user_interface()