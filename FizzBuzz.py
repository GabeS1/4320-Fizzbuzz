n = -1
while(n < 0):
    n = int(input("Enter max POSITIVE amount of numbers to Fizzbuzz: "))

for i in range (1,n+1):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print (i)