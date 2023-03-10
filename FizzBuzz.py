n = -1   #setting n equal negative number since it needs to be less than 0 in the while code below
while(n < 0):  
    n = int(input("Enter max POSITIVE amount of numbers to Fizzbuzz: ")) #Made this so as long as the user input is a positive number it will be used and the code below aka FizzBuzz will be applied.

for i in range (1,n+1):    #Here I implemented the user input which is n and added 1 to it because in order for it to use the number it is prompted to it will need to be one higher than what is wanted.
    if (i % 3) == 0:       
        print("Fizz")      #if number is a multiple of 3 it will be changed to Fizz
    elif (i % 5) == 0:
        print("Buzz")      #if a number is a multiple of 5 it will be changed to Buzz
    elif (i % 3) == 0 and i % 5 == 0:
        print("FizzBuzz")  #if a number is a multiple of 3 and 5 it will be changed to FizzBuzz
    else:
        print (i)          #anything else that is not apart of the parameters set above will be just be written as normal.