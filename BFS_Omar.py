graph = {
    "A": ["B", "C"],
    "B": ["A", "F"],
    "C": ["A", "D", "E", "F"],
    "D": ["C"],
    "E": ["C", "G"],
    "F": ["B", "C"],
    "G": ["E"]
}

goal = input("Enter target: ")
goal = goal.upper()

openList = []
closeList = []

openList.append(("\\", "A"))

check = True
found = False

while(check):
    
    if(len(openList) == 0):
        break
        
    node = openList.pop()
    children = graph[node[1]]
    
    if(node[1] == goal):
        found = True
        break
    
    for child in children[::-1]:
        if (node[1], child) not in closeList:
            openList.append((node[1], child))
    
    closeList.append(node)
    
if(found == False):
    print("Goal Not Found")
else:
    print("Goal Found!")
    
print("Open List is: %s" % openList)
print("Close List is: %s" % closeList)