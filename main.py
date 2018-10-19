from graph import graph

def shell(g):
    command = ""
    while command.lower() != "q":
        command = input("> ")
        if command == "critical path":
            start = input ("Start? ")
            end = input("End? ")
            print (g.criticalPath(start, end));
        elif command == "list":
            g.printAdjList()
        print(command)

def main():
    g = graph()
    g.readGraph("test.txt")
    shell(g)

if __name__ == "__main__":
    main()
