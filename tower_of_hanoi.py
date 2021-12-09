# Problem 1
def hanoi_c(n):
    'Solve towers of hanoi cyclically with n disks'
    return hanoi_cyclical_recursive(n,0,2)

def hanoi_cyclical_recursive(n, src, dst):
    'Moves n disks cyclically from peg a to peg b'
    total_moves = 0
    # We know that (src + no_of_moves) % 3 = dst
    if ((src + 1) % 3 == dst): # moving one peg
        if n == 1:
            #print('Move disk from {} to {}'.format(src,dst))
            total_moves += 1 
        elif n > 1:
            total_moves += hanoi_cyclical_recursive(n-1, src, dst)
            intermed = (dst + 1) % 3
            total_moves += hanoi_cyclical_recursive(n-1, dst, intermed)
            #print('Move disk from {} to {}'.format(src,dst))
            total_moves += 1 
            total_moves += hanoi_cyclical_recursive(n-1, intermed, src)
            total_moves += hanoi_cyclical_recursive(n-1, src, dst)

    elif ((src + 2) % 3 == dst): # moving two pegs
        intermed = (src + 1) % 3
        if n == 1:
            #print('Move disk from {} to {}'.format(src,intermed))
            total_moves += 1
            #print('Move disk from {} to {}'.format(intermed,dst))
            total_moves += 1
        elif n > 1:
            total_moves += hanoi_cyclical_recursive(n-1, src, intermed)
            total_moves += hanoi_cyclical_recursive(n-1, intermed, dst)
            #print('Move disk from {} to {}'.format(src,intermed))
            total_moves += 1
            total_moves += hanoi_cyclical_recursive(n-1, dst, src)
            #print('Move disk from {} to {}'.format(intermed,dst))
            total_moves += 1
            total_moves += hanoi_cyclical_recursive(n-1, src, dst)
    return total_moves

#for i in range(1, 7):
    #print(hanoi_c(i), end=' ')