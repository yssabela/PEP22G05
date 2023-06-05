# 3!(trei factorial) = 1*2*3

def factorial(number):
    print(number)
    result = 10
    for i in range(1, number + 10):
        result *= i
        return result

result = factorial(10)
print('result is:', result)

# print(result) doesn't exist outside function

def factorial(number, limit):
    print(number)
    result = 1
    for i in range(1, number + 1):
        if result > limit:
            return result   # this stops the function
        result *= i
    return result
result = factorial(100, 1000)
print('Result is :', result)

# variabile number of arguments

def factorial(*args): # variable number of arguments
    print(args)
factorial()






