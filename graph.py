import math

class graph:
    
    def __init__(self):
        self.adjList = dict()

    # Reads a graph in adjacency list format from a file, allowing duplicate edges.
    def readGraph(self, fileName):
        for line in open(fileName):
            nodes = line.split()
            for i in range(1, len(nodes)):
                # If the node doesn't already exist as a key in the list, python
                # will throw a KeyError, so make sure it exists, or create a new
                # list to store its children in the graph
                if nodes[0] in self.adjList:
                    self.adjList[nodes[0]].append(nodes[i])
                else:
                    self.adjList[nodes[0]] = [nodes[i]]

    # Writes the adjacency list for this run to a file, in such a manner that the program
    # can read it back in
    def writeToFile(self, fileName):
        f = open(fileName, "a")
        for key in self.adjList:
            f.write(key + " ")
            for val in self.adjList[key]:
                f.write(val + " ")
            f.write("\n")

    def addNode(self, nodeName):
        self.adjList[nodeName] = []

    def connect(self, source, dest):
        self.adjList[source].append(dest)

    def findParents(self, node):
        parentsList = []
        for k in self.adjList.keys():
            if node in self.adjList[k]:
                parentsList.append(k)
        return parentsList

    def isInGraph(self, node):
        if node in self.adjList.keys():
            return True
        else: 
            for k in self.adjList.keys():
                if node in self.adjList[k]:
                    return True
        return False

    def getAllNodes(self):
        nodeList = []
        for n in self.adjList.keys():
            if n not in nodeList:
                nodeList.append(n)
            for i in self.adjList[n]:
                if i not in nodeList:
                    nodeList.append(i)
        return nodeList

    def criticalPath(self, start, end):
        # Create a list of all the vertices in the graph with their earliest start times initially set to 0
        # TODO BFS of the graph to initialize would be faster
        earliestStartTimes = dict()
        for node in self.adjList:
            earliestStartTimes[node] = 0
            for n in self.adjList[node]:
                earliestStartTimes[n] = 0

        # Set up the latestStartTimes list
        latestStartTimes = dict()
        for node in earliestStartTimes:
            latestStartTimes[node] = math.inf

        # Compute the earliest start time for each node
        queue = [start]
        while queue:
            currentVert = queue.pop(0)
            if currentVert in self.adjList:
                for vert in self.adjList[currentVert]:
                    earliestStartTimes[vert] = max(earliestStartTimes[vert], earliestStartTimes[currentVert] + 1)
                    queue.append(vert)

        complementGraph = self.getComplement()
        latestStartTimes[end] = earliestStartTimes[end]
        queue = [end]
        while queue:
            currentVert = queue.pop(0)
            if currentVert in complementGraph.adjList:
                for vert in complementGraph.adjList[currentVert]:
                    latestStartTimes[vert] = min(latestStartTimes[vert], latestStartTimes[currentVert] - 1)
                    queue.append(vert)
        
        criticalPath = []
        for v in earliestStartTimes:
#            if earliestStartTimes[v] == latestStartTimes[v]:
                criticalPath.append([v, earliestStartTimes[v], latestStartTimes[v]])
        return criticalPath

    def getComplement(self):
        complement = graph()
        for vert in self.adjList:
            for v in self.adjList[vert]:
                if v in complement.adjList:
                    complement.adjList[v].append(vert)
                else:
                    complement.adjList[v] = [vert]
        return complement

    def printAdjList(self):
        for key in self.adjList:
            print(key + ", " +  str(self.adjList[key]))

