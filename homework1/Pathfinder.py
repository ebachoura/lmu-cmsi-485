'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode
import unittest
from queue import PriorityQueue

class Pathfinder:

    @staticmethod
    def solve(problem):
        frontier = PriorityQueue();
        root = SearchTreeNode(problem.initial, None, None, 0, problem.heuristic(problem.initial))
        frontier.put(root)
        closedList = {}
        x = 0;

        while not frontier.empty():
            current = frontier.get()
            if problem.goalTest(current.state):
                resultList = []
                while current.parent != None:
                    resultList.insert(0, current.action)
                    current = current.parent
                print("Number of nodes visited: " + str(x))
                print("Number of nodes left in frontier: " + str(frontier.qsize()))
                return resultList
            closedList[current.state] = 1
            generatedNodes = problem.transitions(current.state)
            for node in generatedNodes:
                if not node[2] in closedList:
                    newNode = SearchTreeNode(node[2], node[0], current, current.totalCost + node[1], problem.heuristic(node[2]))
                    current.children.append(newNode)
                    frontier.put(newNode)
                    x += 1
        return None

class PathfinderTests(unittest.TestCase):
    # def test_maze1(self):
    #     maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 4)
    #
    # def test_maze2(self):
    #     maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 4)
    #
    # def test_maze3(self):
    #     maze = ["XXXXX", "X..GX", "X.MMX", "X*..X", "XXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 4)
    #
    # def test_maze4(self):
    #     maze = ["XXXXXX", "X....X", "X*.XXX", "X..XGX", "XXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     self.assertFalse(soln)
    #
    # def test_maze5(self):
    #     maze = ["XXXXXXX", "X.....X", "X..XX.X", "XGX...X", "XXX.XXX", "X*....X", "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 14)
    #
    # def test_maze6(self):
    #     maze = ["XXXXXXXX", "X.....*X", "X.XXXXXX", "X......X", "XXXXXX.X", "XG.....X", "XXXXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 19)
    #
    # def test_maze7(self):
    #     maze = ["XXXXXXX", "X*....X", "X.XXX.X", "X.XXX.X", "X.XXX.X", "X....GX", "XXXXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 8)
    #
    # def test_maze8(self):
    #     maze = ["XXXXX", "XX.GX", "XG.XX", "X..*X", "XXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 3)
    #
    # def test_maze9(self):
    #     maze = ["XXXXX", "XGGGX", "XG*GX", "XGGGX", "XXXXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     solnTest = problem.solnTest(soln)
    #     self.assertTrue(solnTest[1])
    #     self.assertEqual(solnTest[0], 1)
    #
    # def test_maze10(self):
    #     maze = ["XXX", "XGX", "XXX", "X*X", "XXX"]
    #     problem = MazeProblem(maze)
    #     soln = Pathfinder.solve(problem)
    #     self.assertFalse(soln)

    def test_maze11(self):
        maze = ["XXXXXXXXXXXXXXXXXXXXXXXX",
                "XG.X................XXXX",
                "XX.X*XXXXXXXXXX.XXX...XX",
                "X..XXX.......XX.X.XXX.XX",
                "XX...XXXXXXX.XX.X.....XX",
                "X.X..X.....X.XXXXXX.XXXX",
                "X.XX.X.X.X.X.XX...X..XXX",
                "X....X.X.X.X.XX.X.XX.XXX",
                "XXXX...X.X......X....XXX",
                "XXXXXXXXXXXXXXXXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 64)

if __name__ == '__main__':
    unittest.main()
