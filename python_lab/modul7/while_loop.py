# 1. Example of using while loops in Python

n = 1

while n < 5:
    print("Hello Pythonista")
    n = n + 1

# 2. Example of using the break statement in while loops
# In Python, we can use the break statement to end a while loop prematurely.

n = 1

while n < 5:
    print("Hello Pythonista")
    n = n + 1
    if n == 3:
        break

# 3. Example of using the continue statement in while loops
# In Python, we can use the continue statement to stop the current iteration of the while loop and
# continue with the next one.

n = 1

while n < 5:
    if n == 2:
        n = n + 1
        continue
    print("Hello Pythonista")
    n = n + 1

# 4. Using if-elif-else statements inside while loop

z = 0

while z < 3:
    if z == 0:
        print("z is", z)
        z += 1
    elif z == 1:
        print("z is", z)
        z += 1
    else:
        print("z is", z)
        z += 1

# 5. Adding elements to a list using while loop

myList = []
i = 0

while len(myList) < 4:
    myList.append(i)
    i += 1

print(myList)

# 6. Python while loop to print a number series

n = 10

while n <= 100:
    print(n, end=",")
    n = n + 10

# 7. Printing the items in a tuple using while loop

myTuple = (10, 20, 30, 40, 50, 60)
i = 0

while i < len(myTuple):
    print(myTuple[i])
    i += 1

# 8. Finding the sum of numbers in a list using while loop

myList = [23, 45, 12, 10, 25]
i = 0
sum = 0

while i < len(myList):
    sum += myList[i]
    i += 1

print(sum)

# 9. Popping out elements from a list using while loop

fruitsList = ["Mango", "Apple", "Orange", "Guava"]

while fruitsList:
    print(fruitsList.pop())

print(fruitsList)

# 10. Printing all letters except some using Python while loop

i = 0
word = "Hello"

# print all letters except y and o

while i < len(word):
    if word[i] == "e" or word[i] == "o":
        i += 1
        continue

    print("Returned letter", word[i])
    i += 1

# 11. Python while loop to take inputs from the user

n = int(input("Enter a number: "))

while n != 0:
    n = int(input("Enter zero to quit: "))

# 12. Converting numbers from decimal to binary using while loop

num = int(input("Enter a number: "))
b = 0
p = 1
n = num

while n > 0:
    rem = n % 2
    b += rem * p
    p = p * 10
    n = n // 2

print("Binary value: ", b)

# 13. Finding the average of 5 numbers using while loop

p = 5
sum = 0
count = 0

while p > 0:
    count += 1
    f = int(input("Enter the number "))
    sum += f
    p -= 1

average = sum / count
print("Average of given Numbers:", average)

# 14. Printing the square of numbers using while loop

n = 1

while n <= 5:
    squareNum = n ** 2
    print(n, squareNum)
    n += 1

# 15. Finding the multiples of a number using while loop

n = int(input("Enter an integer: "))

i = 1
while i <= 10:
    mul = i * n
    i += 1
    print(mul)

# 16. Reversing a number using while loop in Python

n = int(input("Enter a number: "))
rev = 0

while n != 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

print("Reversed number:", rev)

# 17. Finding the sum of even numbers using while loop

i = 0
sum = 0
n = int(input("Enter the number n: "))

while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1

print("Sum of even numbers till n:", sum)

# 18. Finding the factorial of a given number using while loop

n = int(input("Enter the number: "))
f = n
r = 1

while f != 0:
    r *= f
    f -= 1
print("Factorial of", n, "is:", r)
