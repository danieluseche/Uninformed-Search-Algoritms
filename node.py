class Node:

    def __init__(self,name , cost, parent_id):
        self.name = name
        self.cost = cost
        self.parent_id = parent_id

    def __str__(self):
        return f"Node: {self.name}"+"\n"+\
                f"Cost: {self.cost}"+"\n"+\
                f"Parent: {self.parent_id}"+"\n"

    def __lt__(self, x):
        if self.cost < x.cost:
            return True
        else:
            return False

    def __le__(self, x):
        if self.cost <= x.cost:
            return True
        else:
            return False

    def __gt__(self, x):
        if self.cost > x.cost:
            return True
        else:
            return False
    
    def __ge__(self, x):
        if self.cost >= x.cost:
            return True
        else:
            return False
        
