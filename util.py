import random

class Node:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def __str__(self):
        return str(self.getName())

class Edge:
    def __init__(self, source, destination):
        '''
        source and destination are Node instances 
        '''
        self.source = source
        self.destination = destination
    
    def getSource(self):
        return self.source
    
    def getDestination(self):
        return self.destination

    def __str__(self):
        return f'{self.source.getName()} --> {self.destination.getName()}'
    
    def isChildOf(self, node1, node2):
        """
        returns True if node2 is a child of node2 else False
        """
        pass

class Digraph:
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        dest = edge.getDestination()
        source = edge.getSource()
        if not (dest in self.edges and source in self.edges):
            raise ValueError('node not in graph') 
        else:
            self.edges[source].append(dest)
    
    def isChildOf(self, node1, node2):
        if not (node1 in self.edges and node2 in self.edges):
            raise ValueError('node not in graph') 
        else:
            return node2 in self.edges[node1]
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + " -> " + dest.getName() + "\n"
            
        return result[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

class Sequence:
    def __init__(self):
        self.nodes = []
    
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)

    def distanceBetween(self, node1, node2):
        if not (node1 in self.nodes and node2 in self.nodes):
            raise ValueError('No such nodes in sequence')
        else:
            return abs(self.nodes.index(node1) - self.nodes.index(node2))
    
    def mutate(self, k):
        nodes = self.nodes[:k] + self.nodes[k:][::-1]
        res = Sequence()
        res.nodes = nodes
        return res
    
    def __str__(self):
        
        return f"[{', '.join([node.getName() for node in self.nodes])}]"

def sumOfDistances(graph, sequence):
    sum = 0
    
    for i in range(len(sequence.nodes)):
        if i + 1 < len(sequence.nodes):
            for node in sequence.nodes[i+1:]:
                if graph.isChildOf(sequence.nodes[i], node):
                    sum += sequence.distanceBetween(sequence.nodes[i], node)
    
    return sum






def bestAndWorst(G, sequences):
    sequences = sorted(sequences, key=lambda x: sumOfDistances(G, x))
    best = sumOfDistances(G, sequences[0])
    worst = sumOfDistances(G, sequences[-1])
    bestSeqs = []
    worstSeqs = []
    for seq in sequences:
        if sumOfDistances(G, seq) == best:
            bestSeqs.append(seq)
        elif sumOfDistances(G, seq) == worst:
            worstSeqs.append(seq)
    if bestSeqs and worstSeqs:
        return random.choice(bestSeqs), random.choice(worstSeqs)
    else:
        return sequences[0], sequences[-1]


def genAlgo(graph, sequences):
    for i in range(1, len(graph.edges)):
        print(f'Generation {i}:')
        for seq in sequences:
            print(seq, sumOfDistances(graph, seq))
        best, worst = bestAndWorst(graph, sequences)
        print(f'the best ch: {best} | the worst ch: {worst}')
        sequences.remove(worst)
        new = best.mutate(i)
        print(f'mutatet new ch: {new}')
        sequences.append(new)
        print()
    
    # return bestAndWorst(graph, sequences)[0]
    print(f'final best ch: {bestAndWorst(graph, sequences)[0]} with distance: {sumOfDistances(graph, bestAndWorst(graph, sequences)[0])}')
    

############## First Case ########################
'''
G = Graph()
for i in [2, 5, 3, 1, 4]:
    G.addNode(Node(str(i)))

G.addEdge(Edge(G.getNode('1'), G.getNode('5')))
G.addEdge(Edge(G.getNode('1'), G.getNode('4')))
G.addEdge(Edge(G.getNode('1'), G.getNode('3')))
G.addEdge(Edge(G.getNode('4'), G.getNode('2')))


Seq1 = Sequence()
Seq2 = Sequence()
Seq3 = Sequence()


for i in [1, 2, 3, 4, 5]:
    Seq1.addNode(G.getNode(str(i)))

for i in [2, 1, 3, 4, 5]:
    Seq2.addNode(G.getNode(str(i)))

for i in [5, 2, 3, 4, 1]:
    Seq3.addNode(G.getNode(str(i)))

genAlgo(G, [Seq1, Seq2, Seq3])
'''
############## Second Case ########################

G1 = Graph()
for i in [1, 2, 3, 4, 5, 6]:
    G1.addNode(Node(str(i)))

G1.addEdge(Edge(G1.getNode('2'), G1.getNode('1')))
G1.addEdge(Edge(G1.getNode('2'), G1.getNode('6')))
G1.addEdge(Edge(G1.getNode('2'), G1.getNode('5')))
G1.addEdge(Edge(G1.getNode('2'), G1.getNode('4')))
G1.addEdge(Edge(G1.getNode('1'), G1.getNode('4')))
G1.addEdge(Edge(G1.getNode('6'), G1.getNode('3')))

Seq1 = Sequence()
Seq2 = Sequence()
Seq3 = Sequence()
Seq4 = Sequence()



for i in [6, 5, 4, 3, 2, 1]:
    Seq1.addNode(G1.getNode(str(i)))

for i in [6, 1, 4, 3, 2, 5]:
    Seq2.addNode(G1.getNode(str(i)))

for i in [6, 5, 1, 2, 4, 3]:
    Seq3.addNode(G1.getNode(str(i)))

for i in [6, 2, 1, 4, 3, 5]:
    Seq4.addNode(G1.getNode(str(i)))

genAlgo(G1, [Seq1, Seq2, Seq3, Seq4])


############## Third Case ########################
'''
Seq1 = Sequence()
Seq2 = Sequence()
Seq3 = Sequence()
Seq4 = Sequence()


for i in [4, 6, 5, 3, 2, 1]:
    Seq1.addNode(G1.getNode(str(i)))

for i in [4, 1, 2, 3, 5, 6]:
    Seq2.addNode(G1.getNode(str(i)))

for i in [2, 1, 4, 5, 6, 3]:
    Seq3.addNode(G1.getNode(str(i)))

for i in [2, 6, 5, 1, 4, 3]:
    Seq4.addNode(G1.getNode(str(i)))

genAlgo(G1, [Seq1, Seq2, Seq3, Seq4])

'''






