#                                         performed in 'FOR' and 'WHILE' loops

# FOR LOOPS - a list, a tuple, a dictionary, a set, or a string)

# LOOP THROUGH ITERATION -- TUPLE
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

# LOOP THROUGH ITERATION -- STRING
for x in "banana":
    print(x)
# LOOP THROUGH ITERATION -- DICT
days = {'mon': 'monday', 'tue': 'tuesday', 'wed': 'wednesday', 'thurs': 'thursday', 'fri': 'friday', }
for day in days:
    print(day, 'stands for', days[day])

# RANGE FUNCTION -  0 is default start, and goes up to, not including last number
for i in range(1, 11):
    print(i)
# can use range function to loop through a range by a certain number .eg showing like a times table
for x in range(2, 30, 3):
    print(x)
# started at 2 - went up to, not including 30, adding 3 (last value) each time


# BREAK STATEMENT IN LOOP  - completely break out of a loop (stops it)
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('found it')
        break
    print(num)

# printed out 1 and 2 as it didn't meet the conditional but when it hit 3 and met the conditional it printed 'found it'
# and broke out of the for loop.
# if there is else statement and loop is break then it will not excecuted


# CONTINUE STATEMENT IN LOOP - moves on to the next iteration(skips/ignores to the next)
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print('found it')
        continue
    print(num)
# as soon as it hit continue it carried on to the next

# LOOP IN A LOOP, NESTED LOOP
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

# looped through first value and then looped through every value in inner loop and then went back to second value of
# outer loop gave us every value

#  two arguments that will return an array of the first (n) multiples of (x).
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


# WHILE LOOPS
i = 0
while i < 0:
    print(i)
    i += 1
# while i is less than 6 print i, then add 1

# WHILE AND ELSE STATEMENT
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

