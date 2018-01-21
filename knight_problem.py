from collections import deque

def search(n,x,y):

    todo = deque([((0,0),0)]) #x,y,move_count
    visited = set()
    end = (n-1,n-1)

    while todo:
        (a,b),move_count = todo.popleft()
        new_move_count = move_count + 1
        new_moves = set((
            (a + x, b + y),
            (a + y, b + x),
            (a + x, b - y),
            (a + y, b - x),
            (a - x, b + y),
            (a - y, b + x),
            (a - x, b - y),
            (a - y, b - x)))
        new_moves_filtered = ((i,j) if i<j else (j,i) for (i,j) in new_moves if 
                0 <= i < n and 0 <= j < n)

        for new_move in new_moves_filtered:
            if new_move == end:
                return new_move_count
            if new_move not in visited:
                visited.add(new_move)
                todo.append((new_move,new_move_count))
    #can't reach destination
    return -1


def print_results(n):
    already_done = {(1,1):n-1}
    r = range(1,n)
    for i in r:
        results = []
        for j in r:
            param = (i,j) if i<j else (j,i)
            if param in already_done:
                results.append(already_done[param])
            else:
                result = search(n,i,j)
                already_done[param] = result
                results.append(result)
        print(' '.join(str(result) for result in results))

