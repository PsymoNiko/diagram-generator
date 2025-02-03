from graphviz import Digraph
from pyfiglet import Figlet

def create_diagram():
    fig = Figlet(font='slant')
    print(fig.renderText("Network Diagram"))
    
    dot = Digraph(format="png")
    nodes = {1: "ali", 2: "mamad"}
    comments = {1: ["salam"], 2: []}
    
    while True:
        print("\nOptions:")
        print("1. View added nodes")
        print("2. Add or remove comments")
        print("3. Define connections between nodes")
        print("4. Generate diagram and exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            print("\nNodes list:")
            for num, name in nodes.items():
                print(f"{num}: {name}")
        
        elif choice == "2":
            print("\nNow manage comments for nodes.")
            while True:
                print("\nCurrent Nodes:")
                for num, name in nodes.items():
                    print(f"{num}: {name}")
                
                command = input("Enter a command (or type 'done' to return to menu): ").strip()
                if command.lower() == "done":
                    break
                
                if command.startswith("+"):
                    try:
                        parts = command.split(" ", 1)
                        node_number = int(parts[0][1:].strip())
                        description = parts[1] if len(parts) > 1 else ""
                        if node_number in nodes:
                            comments[node_number].append(description)
                            print(f"Added comment to {nodes[node_number]}: {description}")
                        else:
                            print("Invalid node number! Try again.")
                    except (ValueError, IndexError):
                        print("Invalid format! Use +number comment to add a comment.")
                
                elif command.startswith("-"):
                    try:
                        node_number = int(command[1:].strip())
                        if node_number in nodes and comments[node_number]:
                            print("\nComments for", nodes[node_number], ":")
                            for idx, comment in enumerate(comments[node_number], start=1):
                                print(f"{idx}: {comment}")
                            
                            comment_idx = int(input("Enter the number of the comment to remove: ").strip()) - 1
                            if 0 <= comment_idx < len(comments[node_number]):
                                removed_comment = comments[node_number].pop(comment_idx)
                                print(f"Removed comment from {nodes[node_number]}: {removed_comment}")
                            else:
                                print("Invalid comment number! Try again.")
                        else:
                            print("No comments found for this title or invalid node number.")
                    except ValueError:
                        print("Invalid format! Use -number to remove a comment.")
        
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

