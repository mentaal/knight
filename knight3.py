import logging
logger = logging.getLogger()
class Node:

    def __init__(self, coord=(0,0), previous=None,move_count=0):
        self.coord = coord
        self.previous = previous
        self.move_count = move_count

    def __repr__(self):
        coord = self.previous.coord if self.previous is not None else 'None'
        return "Node(coord={},previous={},move_count={})".format(
                self.coord,
                coord,
                self.move_count)

class Crawler:

    def __init__(self, param ,n):
        x,y = param
        self.moves = (
                (x, +y),
                (y, +x),
                (x, -y),
                (y, -x),
                (-x, +y),
                (-y, +x),
                (-x, -y),
                (-y, -x))
        self.param = param
        logger.debug("Using crawler with n set to: %d", n)
        self.n = n
        self.end = (n-1,n-1)
        self.max_moves = n*n
        self.best = self.max_moves
        self.move_history = {}


    def next_move(self, node):
        "make this a generator"
        logger.debug("In next move, with %s as node arg...", node)
        a,b = node.coord
        n = self.n
        new_moves_gen = [(a+x, b+y) for (x,y) in self.moves]
        new_moves_filtered = set((a,b) if a<b else (b,a) for (a,b) in new_moves_gen
                                    if (0 <= a < n) and (0 <= b < n))
        logger.debug("New moves: %s", new_moves_filtered)

        new_move_count = node.move_count + 1

        for coord in new_moves_filtered:
            logger.debug("Checking new coord: %s", str(coord))
            old_move = self.move_history.get(coord)
            if old_move is not None:
                logger.debug("Found old move with move_count: %d. Current move count: %d", old_move.move_count, node.move_count)
                if old_move.move_count <= new_move_count:
                    logger.debug("Got new coord but it's already been visited: %s with <= move count so skipping", old_move)
                    continue
            new_node = Node(coord, node, new_move_count)
            self.move_history[coord] = new_node
            logger.debug("returning new node: %r", new_node)
            return new_node
        logger.debug("From %r, can find no more nodes", node)
        return None

    def crawl(self):
        n = Node()
        max_moves = self.max_moves
        go_back = False

        while True:
            if go_back:
                go_back = False
                previous = n.previous
                if previous is None:
                    logger.debug("Finished searching. Returning best result: %d", self.best)
                    best = self.best
                    return -1 if best == max_moves else best # we're done
                n = previous
            elif n.coord == self.end:
                count = n.move_count
                if count < self.best:
                    self.best = count
                    logger.debug("Found new best in %d moves", count)
                    go_back = True
                    continue

            new_node = self.next_move(n)
            if new_node is None:
                go_back = True
            else:
                n = new_node

def print_results(n):
    arg_history = {(1,1):n-1}
    r = range(1,n)

    for i in r:
        line_results = []
        for j in r:
            logger.debug("Now getting result for param: (%d,%d)", i,j)
            coord = (i,j) if i<j else (j,i)
            result = arg_history.get(coord)
            if result is None:
                result = Crawler(coord,n).crawl()
                arg_history[coord] = result
            line_results.append(result)
        print(" ".join(str(num) for num in line_results))

