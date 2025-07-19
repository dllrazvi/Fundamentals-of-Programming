#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions.
import math
def add_new_number(numbers:list,s:str):
        #r=int(s[0])
        #if s[1]=='-':
        #    i=-int(s[2])
        #else:
        #    i=int(s[2])
        #numbers.append([r,i])
        assert type(s)==str, "Wrong number"
        numbers.append(s)

def display_all_list(numbers:list):
   print(numbers)
def add_new_number_at_position(numbers:list,s:str,p:int):
    #r = int(s[0])
    #if s[1] == '-':
     #   i = -int(s[2])
    #else:
    #    i = int(s[2])
    assert p>=0 and p<len(numbers), "Wrong index"
    numbers.insert(p,s)
def remove_number_at_position(numbers:list,p:int):
    c=[]
    assert type(p)==int,"Wrong position"
    assert p>=0 and p<len(numbers), "Wrong index"
    for i in range (0,len(numbers)):
        if i != p:
            c.append(numbers[i])
    numbers.clear()
    numbers.extend(c) #copy c in numbers
def remove_multiple_numbers(numbers:list,start:int,end:int):
    c = []
    #if start != 0:
    #    c.append(numbers[:start])
     #   c.append(numbers[end:])
    #else:
    #    c.append(numbers[end+1:])
    assert type(start)==int and type(end)==int, "invalid index"
    assert start>=0 and start<len(numbers) and end>=0 or end<=len(numbers) and start<end, "Wrong index"
    for i in range(0, len(numbers)):
        if i < start or i > end:
            c.append(numbers[i])
    numbers.clear()
    numbers.extend(c)  # copy c in numbers
def replace_number(numbers:list,s:str,r:str):
    c=[]
    ok=False
    assert type(s)==str and type(r)==str,"wrong numbers"
    for i in range (0,len(numbers)):
        if numbers[i] != s:
            c.append(numbers[i])
        else:
            c.append(r)
            ok = True
    assert ok==True, "Number not found"
    numbers.clear()
    numbers.extend(c)
def list_real(numbers:list,start:int,end:int):
    assert start>=0 and start<len(numbers) and end>=0 and end<len(numbers) and start<end, "Wrong index"
    ok=False
    for i in range(start,end):
        a,b=numbers[i]
        if b == 0:
            print(a)
            ok=True

    assert ok == True, "No real numbers found"

def list_modulus(numbers:list,complex:list,s:str,n:int):
    assert s=='<' or s=='=' or s=='>', "Wrong sign number"
    assert n>0 and n!=0 , "Wrong modulo. Either negative or sqrt(0)"
    if s == '=':
        ok=False
        for i in range(0,len(numbers)-1):
            a,b=numbers[i]
            if math.sqrt(a*a+b*b) == n:
                print(complex[i])
                ok=True
        assert ok == True, "No complex numbers matching the condition"

    elif s == '<':
        ok = False
        for i in range(0, len(numbers)-1):
            a, b = numbers[i]
            if math.sqrt(a*a+b*b) < n:
                print(complex[i])
                ok = True

        assert ok==True,"No complex numbers matching the condition"
    elif s == '>':
        ok = False
        for i in range(0, len(numbers)-1):
            a, b = numbers[i]
            if math.sqrt(a*a+b*b) > n:
                print(complex[i])
                ok = True
        assert ok==True,"No complex numbers matching the condition"
def filter_real(numbers:list,complex:list):
    c = []
    f = []
    ok = False
    for i in range(0, len(numbers)):
        a,b=numbers[i]
        if b == 0:
            f.append(numbers[i])
            c.append(complex[i])
            ok = True
        else:
            complex.clear()
            complex.extend(c)
            numbers.clear()
            numbers.extend(f)
    assert ok == True, "There does not exist real numbers ( imaginary = 0 )"


def filter_modulo(numbers:list,complex:list,s:str,n:int):
    c = []
    f = []
    ok = False
    assert s == '<' or s == '=' or s == '>', "Wrong sign number"
    assert n > 0 and n != 0, "Wrong modulo. Either negative or sqrt(0)"
    if s == '=':
        ok = False
        for i in range(0, len(numbers)-1):
            a, b = numbers[i]
            if math.sqrt(a * a + b * b) == n:
                f.append(numbers[i])
                c.append(complex[i])
                ok = True
        assert ok==True,"No complex numbers matching the condition"
    elif s == '<':
        ok = False
        for i in range(0, len(numbers)-1):
            a, b = numbers[i]
            if math.sqrt(a * a + b * b) < n:
                f.append(numbers[i])
                c.append(complex[i])
                ok = True
        assert ok==True,"No complex numbers matching the condition"
    elif s == '>':
        ok = False
        for i in range(0, len(numbers)-1):
            a, b = numbers[i]
            if math.sqrt(a * a + b * b) > n:
                f.append(numbers[i])
                c.append(complex[i])
                ok = True
        assert ok==True,"No complex numbers matching the condition"
    if ok == True:
        complex.clear()
        complex.extend(c)
        numbers.clear()
        numbers.extend(f)