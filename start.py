from graphviz import Digraph

def create_diagram():
    print("\n### Network Diagram Generator ###\n")
    dot = Digraph(format="png")
    nodes = {}
    comments = {}
    
    # Adding nodes
    node_list = []
    while True:
        title = input("Enter a node name (or type 'done' to finish adding nodes): ").strip()
        if title.lower() == "done":
            break
        if title.startswith("-") and title.endswith(";"):
            try:
                node_number = int(title[1:-1])
                if node_number in nodes:
                    print(f"Removing node {nodes[node_number]}")
                    del nodes[node_number]
                    node_list = [n for n in node_list if n != nodes.get(node_number, "")]
                    comments.pop(node_number, None)
                else:
                    print("Invalid node number! Try again.")
            except ValueError:
                print("Invalid input format! Use -number; to remove a node.")
            continue
        
        if title in nodes.values():
            print("Node already exists! Try another name.")
            continue
        
        node_number = len(node_list) + 1
        nodes[node_number] = title
        node_list.append(title)
        dot.node(title, title)
    
    while True:
        print("\nOptions:")
        print("1. View added titles")
        print("2. Add comments/descriptions")
        print("3. Define connections between nodes")
        print("4. Generate diagram and exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            print("\nNodes list:")
            for num, name in nodes.items():
                print(f"{num}: {name}")
        
        elif choice == "2":
            print("\nNow define comments for nodes.")
            while True:
                command = input("Enter a comment command (or type 'done' to return to menu): ").strip()
                if command.lower() == "done":
                    break
                
                if command.startswith("/c;"):
                    try:
                        parts = command.split(" ", 1)
                        node_number = int(parts[0][3:])
                        description = parts[1] if len(parts) > 1 else ""
                        if node_number in nodes:
                            comments[node_number] = description
                            print(f"Comment added to {nodes[node_number]}: {description}")
                        else:
                            print("Invalid node number! Try again.")
                    except (ValueError, IndexError):
                        print("Invalid comment format! Use /c; number description")
                
                elif command.startswith("+/c;"):
                    try:
                        parts = command.split(" ", 1)
                        node_number = int(parts[0][4:])
                        description = parts[1] if len(parts) > 1 else ""
                        if node_number in nodes:
                            comments[node_number] = comments.get(node_number, "") + " " + description
                            print(f"Updated comment for {nodes[node_number]}: {comments[node_number]}")
                        else:
                            print("Invalid node number! Try again.")
                    except (ValueError, IndexError):
                        print("Invalid comment format! Use +/c; number description")
        
        elif choice == "3":
            print("\nNow define connections between nodes by selecting their numbers.")
            while True:
                try:
                    src_num = input("Enter the source node number (or type 'done' to finish adding connections): ").strip()
                    if src_num.lower() == "done":
                        break
                    src_num = int(src_num)
                    if src_num not in nodes:
                        print("Invalid source node number! Try again.")
                        continue
                    
                    dest_num = int(input(f"Enter the destination node number for '{nodes[src_num]}': ").strip())
                    if dest_num not in nodes:
                        print("Invalid destination node number! Try again.")
                        continue
                    
                    dot.edge(nodes[src_num], nodes[dest_num])
                    print(f"Connected {nodes[src_num]} --> {nodes[dest_num]}")
                except ValueError:
                    print("Please enter valid numeric values.")
                    continue
        
        elif choice == "4":
            image_name = input("Enter a filename (without extension, or press Enter for 'network_diagram'): ").strip()
            if not image_name:
                image_name = "network_diagram"
            
            dot.render(image_name)
            print(f"\nDiagram saved as '{image_name}.png'.")
            print("Process completed successfully.")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    create_diagram()

