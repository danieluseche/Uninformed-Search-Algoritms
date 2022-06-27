import sys
import tsplib95
from node import Node
from queue import PriorityQueue

class UniformCostSearch:
    """
        class which solve the Travel Salesman problem
    """
    def __init__(self, TSP):
        self.TSP = TSP 
        self.name = TSP.name #name of the specific TSP problem
        self.cities = list(TSP.get_nodes()) #list all posible cities to travel 
        self.unexplored_cities = self.cities.copy() #in order to compare which cities are in the path to the root

        self.nodeState = Node(name = self.cities[0],\
                         cost = 0,\
                         parent_id = None)
        self.frontier = PriorityQueue(0)
        self.frontier.put(self.nodeState)
        self.explored = set()
        self.solved = False
        self.solution_path = []

    def search(self):

        self.unexplored_cities = self.cities.copy()

        # No solution if the frontier is empty
        if self.frontier.empty():
            return None
        
        # Get the lowest node at frontier:
        self.nodeState = self.frontier.get()
        
        # Add the node to the explored set:
        self.explored.add(self.nodeState)         

        print("*******************************************************************")
        print("Node:")
        print("name:"+ chr(self.nodeState.name + 97))
        print(f"cost: {self.nodeState.cost}")
        #print("Frontier:")
        #print([x.cost for x in self.frontier.queue])

        # Check if the node is a goal State:
        if self.checkGoal(self.nodeState):
            return self.nodeState
        else:
            #add the childs from actual node to fontier
            for city in self.unexplored_cities:
                if city != self.nodeState.name:
                    self.frontier.put(\
                    Node(name = city,\
                    cost = self.nodeState.cost + self.TSP.get_weight(self.nodeState.name, city),
                    parent_id = id(self.nodeState)))


        print("Unexplored: ")
        print([chr(x+97) for x in self.unexplored_cities])
        print("*******************************************************************")
        #search among frontier nodes
        #self.search()

    def checkGoal(self, node):
        
        if node.name in [x for x in self.unexplored_cities]:
            self.unexplored_cities.remove(node.name)
            self.solution_path.append(node.name)


        if node.parent_id == None: #falta implementar el conteo de ciudades
            #print("found root")
            if len(self.unexplored_cities) == 0:
                self.solution_path.reverse()
                self.solved = True
                return True
            else:
                self.solution_path = []
                return False
        
        for parent in self.explored:
            if node.parent_id == id(parent):
                print(f"going from {chr(node.name+97)} to {chr(parent.name+97)}")
                self.unexplored_cities.remove(parent.name)
                self.solution_path.append(parent.name)
                self.checkGoal(parent)
            

    def TSP_load(filepath):
        with open(filepath):
            return tsplib95.load(filepath) 

if __name__=='__main__':
    if len(sys.argv) != 2:
        print("usage:")
        print("    py uniform_cost_tsp.py file.tsp")
        sys.exit(1)

    filepath = sys.argv[1]

    problem = UniformCostSearch(UniformCostSearch.TSP_load(filepath))
    print(f"Problem: {problem.name}\n")

    solution = 0
    while(True):
        solution = problem.search()
        if problem.solved:
            print("*********************SOLVED!!!!***************************** ")
            break;

        if len(problem.frontier.queue) == 0: 
            print("no solution was found")
            break

    print("Solution path:")
    print([chr(x + 97) for x in problem.solution_path])
