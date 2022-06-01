def get_count(sentence):
    return sum(x in 'a,e,i,o,u' for x in sentence)


# RETURN SHORTS LENGTH OF SHORTEST WORD IN STRING
def find_short(s):
    return min(len(x) for x in s.split())


def filter_list(l):
    # 'return a new list with the strings filtered out'
    return [i for i in l if type(i) == int]


S = "ervervige"


#def solution(S):
   # return min(len(x) for x in S not in S.split())

#print(solution(S))

time = 72.345

hours = int(time)
minutes = (time*60) % 60
seconds = (time*3600) % 60

print("%d:%02d.%02d" % (hours, minutes, seconds))