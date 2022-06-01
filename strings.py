# return the count of ALL VOWLS in a string
sentence = 'V>>>VVV'
def get_count(sentence):
    return sum(x in '^><' for x in sentence)

print(get_count(sentence))
# REMOVE FIRST AND LAST CHARACTER OF STRING
def remove_char(s):
    return s[1:-1]
# removing position one and the last


# REPEAT STRING exactly n times.
def repeat_str(repeat, string):
    return repeat * string


# RETURN SHORTS LENGTH OF SHORTEST WORD IN STRING
def find_short(s):
    return min(len(x) for x in s.split())


# RETURN PIN CODES AS STRING LENGTH OF 4 OR 6
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


# RETURN NEW LIST WITH STRINGS OUT OF LIST OF MIX STR AND INT
def filter_list(l):
    # 'return a new list with the strings filtered out'
    return [i for i in l if type(i) == int]


# return value i in list,   for every value i in list if type of i is and integer

# IF STRINGS CONTAIN THE SAME CHARACTERS RETURN TRUE OTHERWISE FALSE
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())


# SORTED() - sorts in a specific order and returns as list,
# sorted both variables in ascending order to compare


#      REVERSE

# REVERSE A SINGLE STRING
x = 'python'
print(x[::-1])
# prints nohtyp
# or
print("".join(reversed(x)))


# REVERSING WORDS IN A STRING
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)


# REVERSE EVERY OTHER WORD IN THE STRING
def reverse_alternate(s):
    words = s.split()
    words[1::2] = [word[::-1] for word in words[1::2]]
    return ' '.join(words)


# REVERSE A LIST




#      REPLACE
# REPLACE MULTIPLE LETTERS IN A STRING - using dict
def DNA_strand(dna):
    char_to_replace = {'A': 'T',
                       'T': 'A',
                       'G': 'C',
                       'C': 'G'}
    dna = dna.translate(str.maketrans(char_to_replace))
    return dna


# or USING TRANSLATE
def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))

#      REMOVE
# REMOVE SPACES FROM STRING, THEN RETURN RESULTANT STRING
def no_space(x):
    return x.replace(' ' ,'')

