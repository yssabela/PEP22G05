# creating a menu using while loop :

def menu():
    print('[1] Option 1')
    print('[2] Option 2')
    print('[3] Exit the program.')


menu()
option = int(input('Enter your option: '))

while option != 0:
    if option == 1:
        # do option 1 stuff
        print('Option 1 has been called! ')
    elif option == 2:
        # do option 2 stuff
        print('Option 2 has bee called! ')
    else:
        print('Invalid option!')

    print()
    menu()
    option = int(input('Enter your option: '))

print('Thanks for using this program! ')


# creating a menu using a function :

def menu():
    print('[1] Option 1')
    print('[2] Option 2')
    print('[3] Option 3')
    print('[0] Exit the program.')

def option3():
    #do option 3 stuff
    print('Option 2 has been called using a function.')

menu()
option = int(input('Enter your option: '))

while option != 0:
    if option == 1:
        # do option 1 stuff
        print('Option 1 has been called! ')
    elif option == 2:
        # do option 2 stuff
        print('Option 2 has bee called! ')
    elif option == 3:
        option3()
    else:
        print('Invalid option!')

    print()
    menu()
    option = int(input('Enter your option: '))

print('Thanks for using this program! ')