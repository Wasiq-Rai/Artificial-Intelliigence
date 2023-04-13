graph = {
    "A" :   [("B",2),("C",4)],
    "B" :   [("A",2),("C",5),("D",1),("F",2)],
    "C" :   [("A",4),("B",5),("D",3),("G",2)],
    "D" :   [("B",1),("C",3),("E",3)],
    "E" :   [("D",3)],
    "F" :   [("B",2)],
    "G" :   [("C",2)]
}

for node in graph:
    graph[node] = sorted(graph[node], key=lambda x: x[1])
start_node = input("What is Starting Node: ")
target_node = input("What is the target node: ")

open = []
close = []



Pair=(start_node, 0)
open.append(Pair)
print("Open :",open)
checked_nodes=0

while target_node not in [node[0] for node in close] :
    print("About to pop a node")
    if len(open) == 0:
        break
    # pair = open[0]
    pair = min(open, key=lambda x: x[1])
    print(pair)
    open.remove(pair)
    node = pair[0]
    print("Node ",node)
    if node not in [node[0] for node in close]:
        print("Node appended in close")
        close.append(pair)
    checked_nodes=checked_nodes+1
    print("Close ",close)
    for goal, cost in graph[node]:
        if goal not in [node[0] for node in close]:
            new_pair = (goal, pair[1] + cost)
            open.append(new_pair)
            print("Open ",open)

print("Close Final UCS: ",close)
print("The Cost to reach goal is :",close[-1][1])
