# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

print()
print("FULL LIST - (for reference):")
print(numbers)

# 1. Print out a list of the even integers:
even = []
for number in numbers:
    if (number % 2) == 0:
        even.append(number)
print()
print("# 1. Print out a list of the even integers:")
print(even)


# 2. Print the difference between the largest and smallest value:
print()
print("# 2. Print the difference between the largest and smallest value:")
print(f"{sorted(numbers)[-1]} - {sorted(numbers)[0]} = {sorted(numbers)[-1] - sorted(numbers)[0]}")


# 3. Print True if the list contains a 2 next to a 2 somewhere.
repeated = False
counter = 0
while (repeated == False) and (counter < len(numbers)-2):
    if numbers[counter] == 2 and numbers[counter+1] == 2:
        repeated = True
    counter += 1

print()
print("# 3. Print True if the list contains a 2 next to a 2 somewhere.")
if repeated:
    print(f"There are two consecutive values equal to '2' - (index {counter-1} and {counter})")
else:
    print("Nope. The list does not contain two '2's next to each other")


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
partial_sum = 0
skip = False
for number in numbers:
    if not(skip):
        if number == 6:
            skip = True
        else:
            partial_sum += number
    else:
        if number == 7:
            skip = False

print()
print("# 4. Print the sum of the numbers, excluding sections between 6s and 7s")
print(partial_sum)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

print()
print("# 5. HARD! Print the sum of the numbers, excluding 13s and whatever number follows it")
print()

counter = 0
partial_sum = 0
skip_next = None

for number in numbers:
    if number == 13:
        skip_next = counter + 1
        print(f"SKIP! - index {counter}: value: {number}")
    elif counter == skip_next:
        print(f"SKIP! - index {counter}: value: {number}")
    else:
        partial_sum += number
        print(f"...adding index {counter}: value: {number} - new sum: {partial_sum}")
    counter +=1

print()
print(f"The final sum is {partial_sum}")

