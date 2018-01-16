from knight import print_results
def test_print_results(request):
    n = request.config.getoption("--board_size")
    print(f"{80*'*'}\nNow on n = {n}\n{80*'*'}\n")
    print_results(n)

move_history = {}
def search(a,b,x,y,n,move_count,max_moves):
    coord = (a,b) if a<b else (b,a)
    other = move_history.get(coord)
    if other is not None:
        if 0 < other < max_moves:
            return other
        else:
            return -1
    move_history[coord] = move_count
    if (a,b) == (n-1,n-1):
        return move_count
    if move_count >= max_moves:
        return -1

    new_move_count = move_count + 1
    new_coords = [ (a + a, b + y),
                   (a + y, b + x),
                   (a + x, b - y),
                   (a + y, b - x),
                   (a - x, b + y),
                   (a - y, b + x),
                   (a - x, b - y),
                   (a - y, b - x)]

    results_gen = (search(c,d,x,y,n,new_move_count,max_moves) for (c,d) in new_coords)
    filtered = [r for r in results_gen if r > 0]
    if len(filtered) > 0:
        return min(filtered)
    else:
        return -1

def test_search():
    r = range(5)
    for i in r:
        results = (search(0,0,i,j,5,0,25) for j in r)
        print(' '.join(str(n) for n in results))
