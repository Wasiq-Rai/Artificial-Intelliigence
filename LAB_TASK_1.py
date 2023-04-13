graph ={
    "A" : ["B","C","E"],
    "B" : "A",
    "C" :  ["A","B","D","E"],
    "E" :  ["A","C"]
}

parent_node = input("Enter Parent node: ")
child_node = input("Enter child node: ")

for key, value in graph.items():
    if child_node in value and key == parent_node :
        print(f"Value {child_node} found in key {key}")
    elif key == parent_node:
        print(f"Value {child_node} NOT found in key {key}")
    elif key != parent_node and child_node not in value:
        print("No such node exists")
        