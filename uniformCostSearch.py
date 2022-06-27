import sys
import tsplib95
from node import Node
from queue import PriorityQueue

class UniformCostSearch:

    def __init__(self, TSP):
        self.TSP = TSP
        self.name = TSP.name
        self.cities = list(TSP.get_nodes())
        self.explored_cities = self.cities

        self.nodeState = Node(name = self.cities[0],\
                         cost = 0,\
                         parent_id = None)
        self.frontier = PriorityQueue(0)
        self.frontier.put(self.nodeState)
        self.explored = set()

    def search(self):
        if self.frontier.empty():
            return None
        
        self.nodeState = self.frontier.get()
        
        if self.checkGoal():
            return self.nodeState

       self.explored.add(self.nodeState)         
       for city in self.cities:
           if city not in self.explored and city not in self.frontier.queue:
               self.frontier.put(\
                       Node(name = city,\
                       cost = self.nodeState.cost + self.TSP.get_weight(self.nodeState, city),
                       parent_name = self.nodeState.name))

           if city in self.frontier.queue:
               pass

    def checkGoal(self, node):
        
        if node.parent_id == None: #falta implementar el conteo de ciudades
            print("found root")
            if len(self.explored_cities) == 0:
                return True
            else:
                self.explored_cities = self.cities
                return False

        for parent in self.explored:
            if node.parent_id == id(parent):
                print(f"going from {self.nodeState.name} to {self.parent.name}")
                self.explored_cities.remove(parent.name)
                self.checkgoal(parent)
            

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
    print(f"Problem: {problem.name}")
