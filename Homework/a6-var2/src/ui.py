#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements)
# are found here
#
import random
import functions
def user_interface():
    numbers=[]
    complex=[]
    cont=True
    for j in range(10):
        r= random.randint(-10,10)
        i= random.randint(-10,10)
        if i>=0:
            complex.append(str(r) + '+' + str(i) + 'i')
        else:
            complex.append(str(r) + str(i) + 'i')
        numbers.append([ r, i])
    print("1. Add a new number [ Syntax: add <number> ]")
    print("2. Insert a new number at a specified position [ Syntax: insert <number> at <position> ]")
    print("3. Remove a number from a specified position [ Syntax: remove <position> ]")
    print("4. Remove numbers from a start position to an end position [ Syntax: remove multiple <start position> to <end position> ]")
    print("5. Replace a number [ Syntax: replace <old number> with <new number> ]")
    print("6. Display all the numbers [ Syntax: list ]")
    print("7. Display the real numbers [ Syntax: list real <start position> to <end position> ]")
    print("8. Display all number with a specified modulo [ Syntax: list modulo [ < | = | > ] <number> ]")
    print("9. Keep only the numbers with imaginary part =0 [ Syntax: filter real ]")
    print("10. Keep only the numbers with a specified modulo [ Syntax: filter modulo [ < | = | > ] <number> ]")
    while cont==True:
        print("The list: ")
        functions.display_all_list(complex)
        option= input("Option: ")
        assert option=='add' or option=='list' or option=='insert' or option=='remove' or option=='remove multiple' or option=='replace' or option == 'list real' or option=='list modulo' or option=='filter real' or option == 'filter modulo', "Wrong option"
        if option == 'add':
            s=str(input("The number to be added: "))
            functions.add_new_number(complex,s)
        elif option == 'list':
            functions.display_all_list(complex)
        elif option == 'insert':
            s=input("The number to be inserted: ")
            try:
                p=int(input("At position: "))
                functions.add_new_number_at_position(complex,s,p)
            except ValueError:
                print("Wrong index")
        elif option == 'remove':
            p=int(input('Position: '))
            functions.remove_number_at_position(complex,p)
        elif option == 'remove multiple':
            start=int(input("Start position: "))
            end=int(input("End position: "))
            functions.remove_multiple_numbers(complex,start,end)
        elif option == 'replace':
            s=input("Which number should be replaced? ")
            r=input("With what number? ")
            functions.replace_number(complex,s,r)
        elif option == 'list real':
            start=int(input("Start position: "))
            end=int(input("End position: "))
            functions.list_real(numbers,start,end)
        elif option == 'list modulo':
            s=input("The sign: ")
            n=int(input("And the number: "))
            functions.list_modulus(numbers,complex,s,n)
        elif option == 'filter real':
            functions.filter_real(numbers,complex)
        elif option == 'filter modulo':
            s = input("The sign: ")
            n = int(input("And the number: "))
            functions.filter_modulo(numbers,complex,s,n)
        option=input("Place a new instruction? [ Syntax: yes / no ]: ")
        assert option=='yes' or option=='no', "Wrong instruction"
        if option =='no':
            cont=False



