# Problem 2
def simple_inversion_count(lst):
    count = 0
    for i in range(len(lst)):
        print(f"Starting i = {i}, count = {count}")
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                count += 1
    return count


import random

# print(simple_inversion_count([random.randint(0,100) for i in range(0,20000)]))
# print(simple_inversion_count([4]))
# print(simple_inversion_count([4,3]))
# print(simple_inversion_count([4,3,1]))
# print(simple_inversion_count([4,3,5,2]))
# print(simple_inversion_count([5,4,3,5,2,1]))
# print(simple_inversion_count([6,5,4,3,5,2,1]))

def merge(L, R):
    'merge two sorted lists L and R into one sorted list'

    i, j = 0, 0
    out = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            out.append(L[i])
            i += 1
        else:
            out.append(R[j])
            j += 1
    if i == len(L):
        out += R[j:]
    else: #j == len(R)
        out += L[i:]
    return out

# longlist_str = open('longlist.txt').read().split(',')
# longlist = [int(i) for i in longlist_str] 

def inversions_recursive(lst):
    count = 0
    if len(lst) == 1:
        return lst, 0

    mid = len(lst)//2
    left_list = lst[:mid]
    right_list = lst[mid:]

    left_sorted, count_l = inversions_recursive(left_list)
    right_sorted, count_r = inversions_recursive(right_list)

    l = 0
    r = 0
    count = count_l + count_r

    while l < len(left_sorted) and r < len(right_sorted):
        if left_sorted[l] <= right_sorted[r]:
            l += 1
        else:
            r += 1
            count += len(left_sorted)-l
    
    return merge(left_sorted, right_sorted), count

# print(inversions_recursive(longlist))
# print(inversions_recursive([4,3]))
# print(inversions_recursive([4,3,1]))
# print(inversions_recursive([4,3,5,2]))
# print(inversions_recursive([4,3,5,2,1]))
# print(inversions_recursive([5,4,3,5,2,1]))
# print(inversions_recursive([6,5,4,3,5,2,1]))

