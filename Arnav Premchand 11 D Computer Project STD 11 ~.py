"""
Computer project for std 11 ~
Name    : Arnav Premchand
Class   : 11 D
Roll No : 10
"""
Main_loop_control_var = 'home'
while Main_loop_control_var == 'home':
    print(' Home ')
    print(" Welcome to Arnav's Menu Driven Program where you can create & operate on a collection of your choice ")
    print(' Enter 1 for Dictionary ')
    print(' Enter 2 for List ')
    print(' Enter 3 for Tuple ')
    Selection1 = int(input(" Enter your choice -> "))
    if Selection1 == 1:
        print(" You chose Dictionary ")
        n = int(input(" Enter number of Key-Value pairs you would like to have "))
        Dk = []
        Dv = []
        while n != 0:
            x = input(" Enter key ")
            Dk.append(x)
            y = input(" Enter Value ")
            Dv.append(y)
            D = dict(zip((Dk), (Dv)))
            n = n - 1
        Dict_loop_control_var = "yes"
        while Dict_loop_control_var == "yes":
            print(' Enter 1 for displaying the Dictionary ')
            print(' Enter 2 for creating a new key value pair ')
            print(' Enter 3 for changing the value of a key ')
            print(' Enter 4 for obtaining the value of a key ')
            print(' Enter 5 for deleting a key-value pair ')
            Selection2 = int(input(" Enter your choice -> "))
            if Selection2 == 1:
                print(D)
            elif Selection2 == 2:
                key = input(" Enter the key ")
                value = input(" Enter the value ")
                D[key] = value
            elif Selection2 == 3:
                key = input(" Enter the key ")
                if D.get(key, 0) == 0:
                    print(" Such a key doesn't exist ")
                else:
                    value = input(" Enter the value ")
                    D[key] = value
            elif Selection2 == 4:
                key = input(" Enter the key ")
                print(' ', D.get(key, " Such a key doesn't exist "))
            elif Selection2 == 5:
                key = input(" Enter the key you would like to delete ")
                if D.get(key, 0) == 0:
                    print(" Such a key doesn't exist ")
                else:
                    del D[key]
                    print(" Modified Dictionary ", D)
            else:
                print(" Error ")
            print(" If you would like to continue enter 'Yes'")
            print(" If you would like to exit the program enter 'Exit' ")
            print(" If you would like to return to home screen enter 'Home' ")
            m1 = input(" Enter your choice -> ")
            m1 = m1.lower()
            m1 = m1.strip()
            Dict_loop_control_var = m1
            if Dict_loop_control_var == 'yes':
                continue
            elif Dict_loop_control_var == 'exit':
                Main_loop_control_var = Dict_loop_control_var
            elif Dict_loop_control_var == 'home':
                break
            else:
                print(" Wrong Input, Returning to Home Screen ")
                continue
    elif Selection1 == 2:
        print(" You chose List ")
        n = int(input(" Enter number of elements you would like to have "))
        L = []
        while n != 0:
            x = eval(input(" Enter the item "))
            L.append(x)
            n = n - 1
        List_loop_control_var = "yes"
        while List_loop_control_var == "yes":
            print(' Enter 1 for displaying the List ')
            print(' Enter 2 for adding a new element ')
            print(' Enter 3 for checking the presence of an element ')
            print(' Enter 4 for deleting an element ')
            Selection2 = int(input(" Enter your choice -> "))
            if Selection2 == 1:
                print(L)
            elif Selection2 == 2:
                x1 = eval(input(" Enter the new element "))
                L.append(x1)
            elif Selection2 == 3:
                x2 = eval(input(" Enter the element "))
                if (x2 in L) is False:
                    print(" Such an item doesn't exist ")
                else:
                    print(" It does exist ")
            elif Selection2 == 4:
                print(L)
                x3 = int(input(" Enter the index of the item you would want to delete from the list "))
                del L[x3]
                print(" Modified List ", L)
            else:
                print(" Error ")
            print(" If you would like to continue enter 'Yes' ")
            print(" If you would like to exit the program enter 'Exit' ")
            print(" If you would like to return to home screen enter 'Home' ")
            m1 = input(" Enter your choice -> ")
            m1 = m1.lower()
            m1 = m1.strip()
            List_loop_control_var = m1
            if List_loop_control_var == 'yes':
                continue
            elif List_loop_control_var == 'exit':
                Main_loop_control_var = List_loop_control_var
            elif List_loop_control_var == 'home':
                break
            else:
                print(" Wrong Input, Returning to Home Screen ")
                continue
    elif Selection1 == 3:
        print(" You chose Tuple ")
        n = int(input(" Enter number of elements you would like to have "))
        T1 = []
        while n != 0:
            x = eval(input(" Enter the item "))
            T1.append(x)
            n = n - 1
        T = tuple(T1)
        Tuple_loop_control_var = "yes"
        while Tuple_loop_control_var == "yes":
            print(' Enter 1 for displaying the Tuple ')
            print(' Enter 2 for adding a new element ')
            print(' Enter 3 for checking the presence of an element ')
            print(' Enter 4 for obtaining index of an element ')
            Selection2 = int(input(" Enter your choice -> "))
            if Selection2 == 1:
                print(T)
            elif Selection2 == 2:
                x1 = eval(input(" Enter the new element "))
                tx1 = (x1,)
                T = T + tx1
            elif Selection2 == 3:
                x2 = eval(input(" Enter the element "))
                if T.count(x2) == 0:
                    print(" It's not there ")
                else:
                    print(" It's there ")
            elif Selection2 == 4:
                print(T)
                x3 = eval(input(" Enter the item whose index you want "))
                if T.count(x3) == 0:
                    print(" Error, The Item is not there ")
                else:
                    print(T.index(x3))
            else:
                print(" Error ")
            print(" If you would like to continue enter 'Yes'")
            print(" If you would like to exit the program enter 'Exit' ")
            print(" If you would like to return to home screen enter 'Home' ")
            m1 = input(" Enter your choice -> ")
            m1 = m1.lower()
            m1 = m1.strip()
            Tuple_loop_control_var = m1
            if Tuple_loop_control_var == 'yes':
                continue
            elif Tuple_loop_control_var == 'exit':
                Main_loop_control_var = Tuple_loop_control_var
            elif Tuple_loop_control_var == 'home':
                break
            else:
                print(" Wrong Input, Returning to Home Screen ")
                continue
    else:
        print(" Wrong Input, Returning to Home Screen ")
        continue
print(" You have exited the program, Thank you & Have a nice day ahead ")
