graph = {
    "A": [("B", 2), ("C", 4)],
    "B": [("A", 2), ("F", 2), ("C", 5), ("D", 1)],
    "C": [("A", 4), ("D", 3), ("B", 5), ("G", 2)],
    "D": [("B", 1), ("C", 3), ("E", 3)],
    "E": [("D", 3)],
    "F": [("B", 2)],
    "G": [("C", 2)]
}

goal = input("Enter target: ")
goal = goal.upper()

openList = []
closeList = []

openList.append(("\\", "A", 0, 0))

check = True
found = False
cost = 0

while(check):
    
    #Don't use break
    if(len(openList) == 0):
        break
        
    node = openList.pop(len(openList) - 1)
    children = graph[node[1]]

    # print("Node =>", node)
    
    if(node[1] == goal):
        found = True
        cost = node[3]
        break
    
    for child in children:
        if (node[1], child[0], child[1]) not in closeList:
            if(node[1], child[0], child[1], child[1] + node[3]) not in openList:
                openList.append((node[1], child[0], child[1], child[1] + node[3]))
    
    if (node[0], node[1], node[2]) not in closeList:
        if(node[1], node[0], node[2]) not in closeList:
            closeList.append((node[0], node[1], node[2]))

    openList.sort(key = lambda x: x[2], reverse=True)
    # print("Open List", openList)
    # print("Close List", closeList)
    
if(found == False):
    print("Goal Not Found")
else:
    print("Goal Found!")
    print("Cost ", cost)
    
print("Open List is: %s" % openList)
print("Close List is: %s" % closeList)