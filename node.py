import math
import connection
class Node:
    def __init__(self,id_numder):
        self.id = id_numder
        self.layer = 0
        self.input_value = 0
        self.output_value = 0
        self.connections : list[connection.Connection] = []

    def activate(self):
        def sigmoid(x):
            return 1/(1 + math.exp(-x))
        
        if self.layer == 1:
            self.output_value = sigmoid(self.input_value)
    
        for i in range(len(self.connections)):
            self.connections[0].to_node.input_value += self.connections[i].weight * self.output_value
    
    def clone(self):
        clone = Node(self.id)
        clone.id = self.id
        clone.layer = self.layer
        return clone