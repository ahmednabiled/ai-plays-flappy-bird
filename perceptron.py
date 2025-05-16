import node
import connection
import random

class Perceptron:
    def __init__(self,inputs : int,clone : bool = False):
        self.connections : list[connection.Connection] = []
        self.nodes : list[node.Node] = []
        self.inputs = inputs
        self.net : list[node.Node] = []
        self.layers = 2

        if not clone :
            for i in range(0,self.inputs):
                self.nodes.append(node.Node(i))

            self.nodes.append(node.Node(3))

            self.nodes.append(node.Node(4))
            self.nodes[4].layer = 1

            for i in range(0 ,4):
                self.connections.append(connection.Connection(self.nodes[i],self.nodes[4],random.uniform(-1,1)))

    def connect_nodes(self):
        for i in range(0,len(self.nodes)):
            self.nodes[i].connections = []

        for i in range(0,len(self.connections)):
            self.connections[i].from_node.connections.append(self.connections[i])
        
    def gen_net(self):
        self.connect_nodes()
        self.net = []
        self.net = sorted(self.nodes,key=lambda x : x.layer)

    def feed_forward(self,vision):
        for i in range(0,self.inputs):
            self.nodes[i].output_value = vision[i]
        
        self.nodes[3].output_value = 1
        for i in range(0,len(self.net)):
            self.net[i].activate()

        output_value = self.nodes[4].output_value

        for i in range(0,len(self.nodes)):
            self.nodes[i].input_value = 0

        return output_value
    
    def clone(self):
        clone = Perceptron(self.inputs, True)

        # Clone all the nodes
        for n in self.nodes:
            clone.nodes.append(n.clone())

        # Clone all connections
        for c in self.connections:
            clone.connections.append(c.clone(clone.getNode(c.from_node.id), clone.getNode(c.to_node.id)))

        clone.layers = self.layers
        clone.connect_nodes()
        return clone

    def getNode(self, id):
        for n in self.nodes:
            if n.id == id:
                return n
            
    def mutate(self):
        if random.uniform(0, 1) < 0.8:
            for i in range(0, len(self.connections)):
                self.connections[i].mutate_weight()