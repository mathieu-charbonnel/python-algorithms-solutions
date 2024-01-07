from collections import deque
'''Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7.  
Note that 3,5 and 7 do not have to be factors but is should not have any other prime factors
For example the first several multiples would be in orders 1, 3, 5, 7, 9, 15, 21'''

def clear(deq, num):
    while deq[0] <= num:
        deq.popleft()
    return deq


def solution(n):
    deques = [deque([3]), deque([5]), deque([7])]
    num = 1
    for k in range(n-1):
        deques = list(map(lambda deq: clear(deq, num), deques))
        candidates = list(map(lambda deq: deq[0], deques))
        ind = candidates.index(min(candidates))
        num = deques[ind].popleft()
        deques[0].append(num * 3)
        deques[1].append(num * 5)
        deques[2].append(num * 7)
    return num

# for i in range(1, 15):
#    print(solution(i))

print(solution(1000000))