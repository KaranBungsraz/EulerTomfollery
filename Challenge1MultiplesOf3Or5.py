# Challenge 1 - Multiples of 3 or 5

# 1. Find all the numbers below 1000

divisibleByThreeList = [] # List for storing all numbers divisible by 3

divisibleByFiveList = [] # List for storing all numbers divisible by 5

for number in range(0,1000): # All numbers between 0 and 1000
    print(number)
    if number % 3 == 0: # If number found is divisible by 3
        numberDivisibleByThree = number # find numbers divisible by 3 and store into the variable "numberDivisibleByThree"
        print("We GOT ONE! Multiples of 3:", numberDivisibleByThree)
        divisibleByThreeList.append(numberDivisibleByThree); # Add each divisible by 3 number to the list so we can add them later
        print("Here's our list for 3s:", divisibleByThreeList)
    elif number % 5 == 0:
        numberDivisibleByFive = number # find numbers divisible by 5 and store into the variable "numberDivisibleByFive"
        print("We GOT ONE AGAIN! Multiples of 5:", numberDivisibleByFive)
        divisibleByFiveList.append(numberDivisibleByFive); # Add each divisible by 3 number to the list so we can add them later
        print("Here's our list for 5s:", divisibleByFiveList)
    else:
        print("WE GOT NOTHING FOOL")

sumOfDivisibleByThree = sum(divisibleByThreeList) # Add up all the numbers in the divisible by 3 list
print("Sum of divisible by 3: ", sumOfDivisibleByThree)

sumOfDivisibleByFive = sum(divisibleByFiveList) # Add up all the numbers in the divisible by 5 list
print("Sum of divisible by 5: ", sumOfDivisibleByFive)

finalResult = (sumOfDivisibleByThree + sumOfDivisibleByFive) # Add both list sums together
print("Final Result: ", finalResult)


