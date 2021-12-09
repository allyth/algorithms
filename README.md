## Problem 1 - tower_of_hanoi.py
A recursive algorithm that for a given number n of disks prints the moves needed to move the disks from peg 0 to peg 2 in a circular, counter-clockwise, model (disks are only allowed to move in a counter-clockwise direction). As a variation, the print statements were commented, so the moves aren't printed, but instead a count of moves is returned.

Run it with:
```
hanoi_c(2)
```

## Problem 2 - inversions.py

1. First, a simple algorithm that counts the number of inversions in a list. An inversion here means a pair of numbers that are in the wrong order, assuming we want the list to be sorted in ascending order.
Run it with:
    ```
    simple_inversion_count([4,3,1])
    ```
2. Following this simple version, a recursive algorithm that counts the number of inversions in a list in time O(n log n). Unlike the simple inversion count algorithm, which struggles with 21,000 elements, the recursive inversion count algorithm performs relatively fast for 1,000,000 elements (26 seconds).

    Run it with:
    ```
    longlist_str = open('longlist.txt').read().split(',')
    longlist = [int(i) for i in longlist_str] 
    inversions_recursive(longlist)
    ```