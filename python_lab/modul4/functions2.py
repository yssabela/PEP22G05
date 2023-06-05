# variables in functions
# global variable in functions
def print_data():
    global my_var
    my_var = 'NewName'
    my_local = 'Local'
    print(f'Global {my_var}')
    def new_print_data():
        nonlocal my_local
        my_local = 'Modified Local'
        print(f'In second function local {my_local}')
        print(f'In second function {my_var}')
    new_print_data()
    print(f'Local var in first function {my_local}')

print(f'outside Global {my_var}')
print_data()
print(f'outside Global {my_var}')
