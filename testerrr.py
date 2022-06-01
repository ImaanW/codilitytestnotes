
def solution(T):
    hour = T // 3600
    minutes = T // 60
    seconds = T % 60
    return f'{hour}h{minutes}m{seconds}s'

print(solution(83643))


def convert(T):
    T = T % (24 * 3600)
    hour = T // 3600
    T %= 3600
    minutes = T // 60
    T %= 60

    return "%d:%02d:%02d" % (hour, minutes, T)

print(convert(83643))

def filter_list(l):
    # 'return a new list with the strings filtered out'
    return [i for i in l if type(i) == int]