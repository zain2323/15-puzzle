import heapq

class Solver:
    class Node:
        def __init__(self, board, previous):
            self.board = board
            self.previous = previous
            if previous is None:
                self.moves = 0
            else:
                self.moves = self.previous.moves + 1
            self.priority = board.manhattan() + self.moves


        def __lt__(self, other):
            return self.priority < other.priority


    def __init__(self, startBoard):
        startNode = self.Node(startBoard, None)
        twinNode = self.Node(startBoard.twin(), None)
        self.explored = []

        pq = []
        twinPq = []

        heapq.heappush(pq, (startNode.priority, startNode))
        # heapq.heappush(twinPq, (twinNode.priority, twinNode))

        while True:
            _, min = heapq.heappop(pq)
            # _, minTwin = heapq.heappop(twinPq)

            if min.board.isGoal():
                print("sol find")
                self.backtrack(min)
                self.printSolution()
                break
            
            # if minTwin.board.isGoal():
            #     print("Not solvable")
            #     break
            
            # Solving the orignal board
            for neighbor in min.board.neighbors():
                if min.previous is None:
                    neighborNode = self.Node(neighbor, min)
                    heapq.heappush(pq, (neighborNode.priority, neighborNode))
                    continue

                if not neighbor.equals(min.previous.board):
                    neighborNode = self.Node(neighbor, min)
                    heapq.heappush(pq, (neighborNode.priority, neighborNode))

            # Solving the twin board
            # for neighbor in minTwin.board.neighbors():
            #     if minTwin.previous is None:
            #         neighborNode = self.Node(neighbor, minTwin)
            #         heapq.heappush(twinPq, (neighborNode.priority, neighborNode))
            #         continue

            #     if not neighbor.equals(minTwin.previous.board):
            #         neighborNode = self.Node(neighbor, minTwin)
            #         heapq.heappush(twinPq, (neighborNode.priority, neighborNode))

    def backtrack(self, node):
        currentNode = node
        while currentNode is not None:
            self.explored.append(currentNode)
            currentNode = currentNode.previous

    def printSolution(self):
        self.explored.reverse()
        print("total moves", len(self.explored))
        for node in self.explored:
            print("***********")
            print(node.board)

from Board import Board

example = [[8, 1, 3], [4,0,2], [7,6,5]]
example = [[8,6,7],[2,5,4],[3,0,1]]
# example = [[1, 2, 3], [4,5,6], [8,7,0]]
# example = [[5,12,4,6],[10,8,15,9],[11,1,13,7], [0,3,2,14]]
# example = [[1, 2, 3, 4], [5, 6, 7, 8], [0, 10, 11, 12], [9, 13, 14, 15]]
board = Board(example)

solver = Solver(board)
