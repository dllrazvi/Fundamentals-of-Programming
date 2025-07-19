def add_newf(code: str, duration: int, depcity: str, destcity: str,flight:list): # this function adds a new flight
    assert len(depcity) <3, "Wrong departure city" # we print in case the input is wrong
    assert len(destcity) <3, "Wrong destination city"
    assert len(code) <3, "Wrong code"
    if duration<20:
        raise ValueError("Flight duration too short")
    else:
        flight.append([code,duration,depcity,destcity]) #if everything is right, we add a new
def delete_flight(code:int,flight:list):
    assert len(code)<3, "Wrong code for flight"
    ok=0
    for i in range(len(flight)):
        if flight[0]==code:
            flight.remove(code)
            ok=1
    if ok==0:
        print("Wrong code")
def citysort(flight:list,destcity:str):
    flight.sort(key=destcity)



