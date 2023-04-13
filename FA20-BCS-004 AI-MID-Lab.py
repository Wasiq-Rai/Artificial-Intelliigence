# FA20-BCS-004
# RAI WASIQ ABDULLAH

# ARTIFICIAL INTELLLIGENCE
# MID LAB EXAM

# 13 APRIL, 2023 


# QUESTION 1:
#     Create following graph in pyhton.

graph ={
    "A" :   ["B","C"],
    "B" :   ["A","D","E"],
    "C" :   ["A","F","G"],
    "D" :   ["B","H"],
    "E" :   ["B","H"],
    "F" :   ["C","H"],
    "G" :   ["C","H"],
    "H" :   ["D","E","F","G"]
}



#   QUESTION 2:
    # Implement and apply DFS on the given graph in such a way that
    #  it should backtrack after third depth,
    #  which means algorithm can only browse thee child node in a given depth up to third level.
    # 
    #  Start node is A and goal node is G.



start_node = 'A'
target_node = 'G'


open      = []
close     = []
forward   = []
backtrack = []



found = False

Pair = ("\\", start_node, 1)  # depth of the start node is 1

open.append(Pair)
# print("Open :", open)


while True:
    if target_node in close:
        found = True

        forward=close.copy()
        temp=close.copy()
        # print("Temp: ",temp)


        # BAcktracking
        node = temp[-1]
        while node != start_node:
            node = temp.pop()
            backtrack.append(node)
            # print("Current Node: ",node)

    if len(open) == 0:
        break
    pair = open.pop()
    node = pair[1]
    depth = pair[2]  # get the depth of the current node
    if node not in close and depth <= 3:  # adding  a condition to check the depth of the node
        close.append(node)
    # print("Close ", close)
    if depth <= 2:  # only add children if depth is less than or equal to 2
        for goal in graph[node][::-1]:
            if goal not in close:
                new_pair = (node, goal, depth + 1)  # incrementing depth by 1 for each child node
                open.append(new_pair)
                # print("Open ", open)
      
     

if found:
    print("----------------------------------------------------------------------------------------------")
    print("______________________________________Depth First Search______________________________________")
    print("\nForward Track: ",forward)
    print("\nBackward Track: ",backtrack)

    close = forward + backtrack

    close.remove(target_node)

    print("\nClose Final DFS: ", close)
    print("\n----------------------------------------------------------------------------------------------")

else:
    print("Target not found")
