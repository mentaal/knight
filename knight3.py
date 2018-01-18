import logging
logger = logging.getLogger()
class Node:

    def __init__(self, a=0,b=0,previous=None,move_count=0):
        self.coord = (a,b) if a<b else (b,a)
        self.previous = previous
        self.move_count = move_count

    def __repr__(self):
        return "Node(a={},b={},previous={},move_count=)".format(
                *self.coord,
                self.previous,
                self.move_count)


class Crawler:
    move_history = {}

    def __init__(self, x,y,n):
        if x>y:
            x,y = y,x
        self.moves = (
                (x, +y),
                (y, +x),
                (x, -y),
                (y, -x),
                (x, +y),
                (y, +x),
                (x, -y),
                (y, -x))
        self.param = x,y
        self.n = n
        self.end = (n-1,n-1)
        self.best = -1


    def next_move(self, node):
        "make this a generator"
        a,b = node.coord
        n = self.n
        new_moves_gen = ((a+x, b+y) for (x,y) in self.moves)
        new_moves_filtered = ((a,b) if a<b else (b,a)
                                if (0 <= a < n) and (0 <= b < n))
        new_move_count = self.move_count + 1

        for coord in new_moves_filtered:
            old_move = self.move_history.get(coord)
            if old_move is not None:
                if old_move.move_count < self.move_count:
                    continue
            new_node = Node(self, *coord, node, new_move_count)
            self.move_history[coord] = new_node
            logger.debug("From %r, returning new node: %r", node, node)
            return new_node
        logger.debug("From %r, can find no more nodes", node)
        return None

    def crawl(self):
        n = Node()
        max_moves = self.max_moves

        while True:
            new_node = self.next_move(n)
            if new_node is None:
                previous = n.previous
                if previous is None:
                    return self.best # we're done
                else:
                    n = previous
            else:
                n = new_node
            if n.coord == self.end:
                self.best = new_node.move_count
                logger.debug("Found end in %d moves", self.best)




