
# RETURN SUM OF MULTIPLES OF 3 OR 5
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# FIZZ BUZZ MUTIIPLES
N = 24
numbers = range(1, N + 1)
for i in numbers:
    if (i % 2 == 0 and i % 3 == 0 and i % 5 == 0):
        print('CodilityTestCoders')
    elif (i % 2 == 0 and i % 3 == 0):
        print('CodilityTest')
    elif (i % 2 == 0 and i % 5 == 0):
        print('CodilityCoders')
    elif (i % 3 == 0 and i % 5 == 0):
        print('TestCoders')
    elif (i % 2 == 0):
        print('Codility')
    elif (i % 3 == 0):
        print('Test')
    elif (i % 5 == 0):
        print('Coders')
    else:
        print(i)
# ensure you have the complex first,
# ensure you have all combinations
# plus one as the N (meaning 24) when using range function it goes up to value, not including
# uses and as you have to tell python what to do, repeat code and be clear
# AND means both are true
# elif - an this , and this
# Else - if not true, excecute this