from collections import namedtuple
acrobat = namedtuple('acrobat', ('height', 'weight'))


# Test cases
case0 = []
case1 = [acrobat(1.8, 78)]
case2 = [acrobat(1.8, 78), acrobat(1.5, 60), acrobat(1.90, 90), acrobat(1.6, 55), acrobat(1.8, 105), acrobat(1.7, 45)]

# Solution to the circus tower problem
def biggestTower(case):
    case.sort(key = lambda x: x.height)
    weight_list = list(map(lambda x: x.weight, case))
    longestEndingHere = [1]
    for w in weight_list[1:]:
        candidate = 0
        for i in range(len(longestEndingHere)):
            if w >= weight_list[i]:
                candidate = max(candidate, longestEndingHere[i] + 1)
            else:
                candidate = max(candidate, longestEndingHere[i])
        longestEndingHere.append(candidate)
    return longestEndingHere[-1]


# Time complexity is O(n**2)
print(biggestTower(case2))
