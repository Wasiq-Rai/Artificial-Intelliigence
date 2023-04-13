graph ={
    "A" :   ["B","C"],
    "B" :   ["A","F"],
    "C" :   ["A","D","E","F"],
    "D" :   ["C"],
    "E" :   ["C","G"],
    "F" :   ["B","C"],
    "G" :   ["E"]
}
# graph ={
#     "A" :   ["B","C"],
#     "B" :   ["F","D"],
#     "C" :   ["A","D","E"],
#     "D" :   ["B","C"],
#     "E" :   ["C","G"],
#     "F" :   ["B","C"],
#     "G" :   ["E"]
# }
# graph ={
#     "A" :   ["B","C"],
#     "B" :   ["A","D"],
#     "C" :   ["A","E"],
#     "D" :   ["B","E"],
#     "E" :   ["C","D"],
# }


open = []
close = []
found =  False
target_node = input("Enter the target Node: ")


Pair=("\\",'A')
new_pair =(0,0)
open.append(Pair)
print("Open :",open)
checked_nodes=0


while True:
    if target_node in close:
        found = True
        break
    if len(open) == 0:
        break
    pair = open.pop()
    # print("Pair ",pair)
    node = pair[1]
    # print("Node ",node)
    if node not in close:
        close.append(node)
    checked_nodes=checked_nodes+1
    print("Close ",close)
    for goal in graph[node] [::-1]:
        if  goal not in close:
            # for value in graph[goal]:
            new_pair = (node, goal)
            # print("New Pair " ,new_pair)
            open.append(new_pair)
            print("Open ",open)

if found:
    print("Close Final DFS: ",close)
else:
    print("Target not found")





    


    
        