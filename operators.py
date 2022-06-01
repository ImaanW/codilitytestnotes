# CONVERT STRING TO NUMBER --
# method turning it from string to integer as method name passes paramenter and same paramter is then called with int
def string_converter(s):
    return int(s)  # or return str() / interger_converter

# calling on the function to test
string_converter(45)
# confirming that the 'type is an int
print(type(string_converter(45)))

#CONVERT STRING TO BOOL
def boolean_to_string(b):
    return str(bool(b)) #or return str(b)

# TAKING IN MULTIPLE OPERATORS IN ONE FUNCTIONS
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 / value2

# INTERATE WITH FORMATTED STRING
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))