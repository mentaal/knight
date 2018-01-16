class Searcher:
    def __init_subclass__(cls, n, a, b, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.max_moves = n*n
        cls.n = n
        cls.move_history = {}
        cls.move_size = (a,b) if a<b else (b,a)

    def __init__(self, a=0, b=0, move_count=0):
        self.coord = (a,b) if a<b else (b,a)
        #print(f"In init for Searcher, a: {a}, b: {b}, self.coord: {self.coord}")
        self.move_count = move_count

    def get_new_moves(self):
        me_a, me_b = self.coord
        a, b = self.move_size

        return (
                (me_a + a, me_b + b),
                (me_a + b, me_b + a),
                (me_a + a, me_b - b),
                (me_a + b, me_b - a),
                (me_a - a, me_b + b),
                (me_a - b, me_b + a),
                (me_a - a, me_b - b),
                (me_a - b, me_b - a))

    def search(self):
        for i in self.coord:
            if not 0 <= i < self.n:
                return -1 #out of bounds
        other = self.move_history.get(self.coord)
        if other is not None and 0 < other.move_count <= self.move_count:
            return -1
        else:
            self.move_history[self.coord] = self #save it
        if self.coord == (self.n-1, self.n-1):
            return self.move_count
        if self.move_count > self.max_moves:
            print("Max moves reached..")
            return -1

        new_move_count = self.move_count + 1

        new_objs = [self.__class__(a,b,new_move_count)
                        for (a,b) in self.get_new_moves()]
        search_result = [o.search() for o in new_objs]
        filtered = [r for r in search_result if r > 0]
        if len(filtered) > 0:
            return min(filtered)
        else:
            return -1


class KnightL:
    def __init_subclass__(cls, n, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.n = n
        cls.call_history = {}
        r = range(1,n)
        params = [(i,j) for i in r for j in r]
        cls.params = params
        cls.param_classes = {p:type('Coord', (Searcher,), {}, n=n,a=p[0],b=p[1])
                                for p in params}

    def get_result(self):
        a,b = self.param
        result = self.result
        if result is None:
            obj = self.param_classes[self.param]()
            result = obj.search()
            self.result = result
            return result
        else:
            return result

    def __init__(self, a, b):
        param = (a,b) if a < b else (b,a)
        self.param = param
        if param in self.call_history:
            other = self.call_history[param]
            self.result = other.result
        else:
            self.call_history[param] = self
            self.result = None

def print_results(n):
    KnightL_class = type('KnightL', (KnightL,), {}, n=n)
    for i in range(0, (n-1)**2, n-1):
        objs = [KnightL_class(*p) for p in KnightL_class.params[i:i+n-1]]
        #print(f"Now on index: {i}, len(objs): {len(objs)}")
        #print(objs)

        print(' '.join(str(obj.get_result()) for obj in objs))
