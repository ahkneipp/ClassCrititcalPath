#TODO convert all of this to use adjecency matrix

class graph:
    
    def __init__(self):
        self.adjList = dict()

    def readGraph(self, fileName):
        for line in open(fileName):
            nodes = line.split()
            if nodes[0] in self.adjList:
                if nodes[1] not in self.adjList[nodes[0]]:
                    self.adjList[nodes[0]].append(nodes[1])
            else:
                self.adjList[nodes[0]] = [nodes[1]]

    def writeToFile(self, fileName):
        f = open(fileName, "a")
        for key in self.adjList:
            for val in self.adjList[key]:
                f.write(key + " " + val + "\n")

    def addNode(self, nodeName):
        self.adjList[key] = []

    def connect(self, source, dest):
        if self.adjList[source] == []:
            self.adjList[source] = [dest]
        else:
            if dest not in self.adjList[source]:
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
        if start in self.adjList.keys() and self.isInGraph(end):
            startTimes = {key: [0,0] for key in self.getAllNodes()}
            nodeQueue = []
            nodeQueue.append(start)
            while nodeQueue:
                if nodeQueue[0] in self.adjList.keys():
                    nodeQueue.extend(self.adjList[nodeQueue[0]])
                    for n in self.adjList[nodeQueue[0]]:
                        startTimes[n][0] = max(startTimes[n][0], startTimes[nodeQueue[0]][0] + 1)
                nodeQueue.pop(0);

            nodeQueue.append(end)
            startTimes[end][1] = startTimes[end][0]
            while nodeQueue:
                parentsList = self.findParents(nodeQueue[0])
                nodeQueue.extend(parentsList)
                for n in parentsList:
                    startTimes[n][1] = max(startTimes[n][1], startTimes[nodeQueue[0]][1] - 1)
                nodeQueue.pop(0)
            
            critPathList = [[start, startTimes[start][0]]]
            for i in startTimes.keys():
                if startTimes[i][0] == startTimes[i][1] and startTimes[i][0] > 0:
                    critPathList.append([i,startTimes[i][0]])
            return critPathList
        else: return []

    def printAdjList(self):
        for key in self.adjList:
            print(key + ", " +  str(self.adjList[key]))
