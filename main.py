from graph import graph
import sys
import argparse


# mode = 0 -> sort by start time
# mode = 1 -> sort by end time
# Bubble sort because there probably isn't any greater than n=50 nodes and It's 2 in the morning and I don't want to
# write merge sort right now
def bubbleSortNodes(nodes, mode):
    for j in range(1, len(nodes)):
        for i in range(j, len(nodes)):
            if nodes[i-1][1 if mode == 0 else 2] > nodes[i][1 if mode == 0 else 2]:
                tmp = nodes[i-1]
                nodes[i-1] = nodes[i]
                nodes[i] = tmp
    return nodes


parser = argparse.ArgumentParser(description='Compute the critical path of a graph supplied in a file')
# Dummy argument to consume the name of the program
parser.add_argument('programName')
# Option arguments
parser.add_argument('-c', help='Only print the critical path', action='store_true')
parser.add_argument('-s', help='Sort by the earliest start time', action='store_true')
parser.add_argument('-e', help='Sort by the earliest end time', action='store_true')
parser.add_argument('-r', help='Reverse the sorting order', action='store_true')
# Required positional arguments
parser.add_argument("scheduleFile", action='store', type=str)
parser.add_argument('startNode', action='store', type=str)
parser.add_argument('endNode', action='store', type=str)


def main():
    g = graph()
    args = vars(parser.parse_args(sys.argv))
    g.readGraph(args['scheduleFile'])
    critPathList = g.criticalPath(args['startNode'], args['endNode'])
    if args['s'] or args['e']:
        critPathList = bubbleSortNodes(critPathList, 0 if args['s'] else 1)
        if args['r']:
            critPathList = critPathList[::-1]
    for node in critPathList:
        if args['c']:
            if node[1] == node[2]:
                print(node)
        else:
            print(node)


if __name__ == "__main__":
    main()
