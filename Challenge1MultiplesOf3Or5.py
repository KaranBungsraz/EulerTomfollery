#Challenge 1 - Multiples of 3 or 5

# 1. Find all the numbers below 1000

divisibleByThreeList = []

divisibleByFiveList = []

for number in range(0,1000):
    number = number + 1
    if number % 3 == 0:
        numberDivisibleByThree = number
        print("We GOT ONE! Multiples of 3:", numberDivisibleByThree)
        divisibleByThreeList.append(numberDivisibleByThree);
        print("Here's our list for 3s:", divisibleByThreeList)
    elif number % 5 == 0:
        numberDivisibleByFive = number
        print("We GOT ONE! Multiples of 5:", numberDivisibleByFive)
        divisibleByFiveList.append(numberDivisibleByFive);
        print("Here's our list for 5s:", divisibleByFiveList)
    else:
        print("WE GOT NOTHING FOOL")

sumOfDivisibleByThree = sum(divisibleByThreeList)
print("Sum of divisible by 3: ", sumOfDivisibleByThree)

sumOfDivisibleByFive = sum(divisibleByFiveList)
print("Sum of divisible by 5: ", sumOfDivisibleByFive)

finalResult = (sumOfDivisibleByThree + sumOfDivisibleByFive) - 1000
print("Final Result: ", finalResult)


