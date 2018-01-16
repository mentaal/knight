import logging
logger = logging.getLogger()
class Searcher:
    def __init__(self,a=0,b=0,move_count=0):
        self.coord = (a,b) if a<b else (b,a)
        self.move_count = move_count

    def search(self):
        coord = self.coord
        a,b = coord
        x,y = self.param
        move_count = self.move_count
        max_moves = self.max_moves
        for o in coord:
            if not 0 <= o < self.n:
                return -1
        other = self.move_history.get(coord, -1)
        if 0 < other < move_count:
            return -1
        self.move_history[coord] = move_count
        if move_count >= max_moves:
            return -1
        if (a,b) == (self.n-1,self.n-1):
            return move_count

        new_move_count = move_count + 1
        if new_move_count >= max_moves:
            return -1

        new_coords = [ (a + x, b + y),
                       (a + y, b + x),
                       (a + x, b - y),
                       (a + y, b - x),
                       (a - x, b + y),
                       (a - y, b + x),
                       (a - x, b - y),
                       (a - y, b - x)]


        results_gen = (self.__class__(a,b,new_move_count).search()
                            for (a,b) in new_coords)
        filtered = [r for r in results_gen if r > 0]
        if len(filtered) > 0:
            return min(filtered)
        else:
            return -1

def searcher_factory(n,param):
    S = type('Searcher', (Searcher,),{})
    S.move_history = {}
    S.n = n
    S.max_moves = n*n-1
    S.param = param
    return S


class Knight:
    def __init__(self,a,b):
        param = (a,b) if a<b else (b,a)
        self.param = param

    def search(self):
        param = self.param
        other = self.call_history.get(param)
        if other is not None:
            print(f"Current param: {param}, getting existing result: {other}")
            return other
        else:
            searcher = searcher_factory(self.n,param)()
            result = searcher.search()
            self.call_history[param] = result
            return result

def knight_factory(n):
    K = type('KnightL', (Knight,), {})
    K.call_history = {}
    K.n = n
    K.max_moves = n*n-1
    return K

def print_results(n):
    K = knight_factory(n)
    r = range(1,n)
    for i in r:
        print(' '.join(str(K(i,j).search()) for j in r))





