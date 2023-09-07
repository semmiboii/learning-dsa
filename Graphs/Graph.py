class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addNode(self,node):
        if node not in self.adjacencyList.keys():
            self.adjacencyList[node] = []
            return True
        return False

    def printGraph(self):
        for node in self.adjacencyList:
            print(node,":",self.adjacencyList[node])

    def addEdge(self,node1,node2):
        self.adjacencyList[node1].append(node2)
        self.adjacencyList[node2].append(node1)

    def removeEdge(self,node1,node2):
        if node1 in self.adjacencyList.keys() and node2 in self.adjacencyList.keys():
            try:
                self.adjacencyList[node1].remove(node2)
                self.adjacencyList[node2].remove(node1)
                return True
            except ValueError:
                pass
            return True
        return False


customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.printGraph()
print("After Adding Edges")
customGraph.addEdge("A","B")
customGraph.addEdge("B","C")
customGraph.addEdge("C","A")
customGraph.printGraph()
print("After removing Edges")
customGraph.removeEdge("A","C")
customGraph.printGraph()
