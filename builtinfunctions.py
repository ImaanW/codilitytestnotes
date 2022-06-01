# BINARY
print(bin(529))


def solution(N):
    binary = str(bin(N))[2:]
    return binary
print(solution(529))

# removes the 0b at start of binary


# ISDIGIT()
def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)
# .STRIP() - remove white space from string

#.UPPER() - uppercase



# FORMAT STRING
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#.append(just joing into list)
#.insert

#SETS
#.ADD -
#.UPDATE - add a whole list
#.Remove


# TRANSLATE/ REPLACE
# .REPLACE("old", "new") - switch characters 1

# string.translate(table) - switch more than 1 and put in table