import operator


def solution_asc(dic):
    sorted_d = sorted(dic.items(), key=operator.itemgetter(0))
    return sorted_d

def solution_desc(dic):
    sorted_d = sorted(dic.items(), key=operator.itemgetter(0),reverse=True)
    return sorted_d

print solution_asc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
print solution_desc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
