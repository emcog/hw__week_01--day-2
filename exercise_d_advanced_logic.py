# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
# adapted from https://code4coding.com/python-program-to-find-odd-and-even-number/

evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(evens)


# 2. Print the difference between the largest and smallest value:

largest = max(numbers)
smallest = min(numbers)
difference = largest - smallest
print(difference)



# 3. Print True if the list contains a 2 next to a 2 somewhere.
# find index of 2, if index -1 || +1 = 2 print true
value = 2
position_of_value = numbers.index(value)
down_stream_of_value = position_of_value - 1
up_stream_of_value = position_of_value + 1

if down_stream_of_value or up_stream_of_value == value:
    print(True)


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# define range start and endpoints, 
# use a loop with < & > to list all the numbers between start and end 
# break filter list down to indexes
# use indexes to remove from array
# total array
# ---- > refactor this so not destructive or original list
unfiltered_total = 0

for number in numbers:
    unfiltered_total += number

print('unfiltered total = ', unfiltered_total)


filter_start = numbers.index(6)
filter_end = numbers.index(7)
filter_counter = filter_start
filter_values = [filter_start]
filtered_total = 0

while filter_counter < filter_end:
    filter_counter += 1
    filter_values.append(filter_counter)
    # filter_values = filter_values.append(filter_counter)

print(filter_values)

for value in filter_values:
    numbers.pop(value)
    
for number in numbers:
    filtered_total += number

print(filtered_total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 