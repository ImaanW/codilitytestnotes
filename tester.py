#replace values in string using dict
sample_string = "This is a sample string"
char_to_replace = {'s': 'X',
                   'a': 'Y',
                   'i': 'Z'}
# Iterate over all key-value pairs in dictionary
for key, value in char_to_replace.items():
    # Replace key character with value character in string
    sample_string = sample_string.replace(key, value)
print(sample_string)