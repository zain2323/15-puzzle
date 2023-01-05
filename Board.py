import copy

class Board:
    def __init__(self, tiles):
        self.n = len(tiles)
        self.tiles = tiles
        self.bx, self.by = self._findLoc(0)
        self.goal = [[1,2,3],[4,5,6],[7,8,0]]
        # self.goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,0]]
        self.map = {
            "1": (0, 0),
            "2": (0, 1),
            "3": (0, 2),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "7": (2, 0),
            "8": (2, 1),
            "0": (2, 2)
        }

        # self.map = {
        #     "1": (0, 0),
        #     "2": (0, 1),
        #     "3": (0, 2),
        #     "4": (0, 3),
        #     "5": (1, 0),
        #     "6": (1, 1),
        #     "7": (1, 2),
        #     "8": (1, 3),
        #     "9": (2, 0),
        #     "10": (2, 1),
        #     "11": (2, 2),
        #     "12": (2, 3),
        #     "13": (3, 0),
        #     "14": (3, 1),
        #     "15": (3, 2),
        #     "0": (3, 3)
        # }

    def __str__(self):
        formatted = ""
        for i in range(self.n):
            for j in range(self.n):
                formatted += str(self.tiles[i][j]) + "   "
            formatted += "\n"
        return formatted
    
    def isGoal(self):
        return self.manhattan() == 0

    def manhattan(self):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] != 0:
                    # x, y = self._findDesiredLoc(self.tiles[i][j])
                    x, y = self.map[str(self.tiles[i][j])]
                    if x == -1 or y == -1:
                        raise Exception("Invalid values supplied")
                    distance += abs(i-x) + abs(j-y)
        return distance

    def _findDesiredLoc(self, entry):
        for i in range(self.n):
            for j in range(self.n):
                if self.goal[i][j] == entry:
                    return (i,j)
        return (-1, -1)
    

    def _findLoc(self, entry):
        for i in range(self.n):
            for j in range(self.n):
                if self.tiles[i][j] == entry:
                    return (i,j)
        return (-1, -1)
    
    def equals(self, board):
        dim = board.n
        if dim != self.n:
            return False
        for i in range(dim):
            for j in range(dim):
                if self.tiles[i][j] != board.tiles[i][j]:
                    return False
        return True

    def neighbors(self):
        neighborsList = []
        
        # Upward direction
        if self.bx != 0:
            neighborsList.append(self._newNeighbor(self.bx, self.by, self.bx - 1, self.by))
        
        # Downward direction
        if self.bx != self.n - 1:
             neighborsList.append(self._newNeighbor(self.bx, self.by, self.bx + 1, self.by))

        # Left
        if self.by != 0:
            neighborsList.append(self._newNeighbor(self.bx, self.by, self.bx, self.by - 1))

        if self.by != self.n - 1:
            neighborsList.append(self._newNeighbor(self.bx, self.by, self.bx, self.by + 1))

        return neighborsList

    def _newNeighbor(self, x1, y1, x2, y2):
        newBoard = copy.deepcopy(self.tiles)
        newBoard[x1][y1], newBoard[x2][y2] = newBoard[x2][y2], newBoard[x1][y1]
        return Board(newBoard)
    
    def twin(self):
        if self.tiles[0][0] != self.tiles[0][1] != 0:
            return self._newNeighbor(0, 0, 0, 1)
        else:
            return self._newNeighbor(1, 0, 1, 1)


    def xyFrom1D(self, i):
        x = i % self.n
        y = i // self.n
        return (x,y)


# example_2 = [[8, 1, 3], [4,0,2], [7,6,5]]
# example = [[1, 2, 3], [4,5,6], [7,8,0]]
# board = Board(example_2)
# print(board.manhattan())
# print(board.equals(example_2))
# print(board._findLoc(0))
# print(board)
# # n = board.neighbors()
# # for b in n:
#     # print("Neighbor")
#     # print(b)
# print(board.twin())

	# private int xyTo1D(int row, int col) {
	# 	return ((col) % width) + (width * (row));

    # 	private int[] xyFrom1D(int i) {
	# 	int [] xy = new int[2];
	# 	xy[0] = i % width; // col
	# 	xy[1] = i / width; // row
	# 	return xy;
	# }