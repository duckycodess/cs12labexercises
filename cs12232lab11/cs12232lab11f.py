from oj import Node

def max_path(root: Node) -> int:
    max_path_sum = float("-inf")
    
    def get_max_gain(node: Node) -> int:
        nonlocal max_path_sum
        if node is None:
            return 0
        
        # Calculate maximum gain from all children
        max_child_gain = 0
        total_child_gain = 0
        for child in node.children:
            child_gain = get_max_gain(child)
            max_child_gain = max(max_child_gain, child_gain)
            total_child_gain += max(0, child_gain)
        
        # Current node value plus maximum gain from any one child
        current_max_gain = node.value + max_child_gain
        
        # Current node value plus all positive gains from children
        current_path_sum = node.value + total_child_gain
        
        # Update the global maximum path sum
        max_path_sum = max(max_path_sum, current_path_sum)
        
        # Return the maximum gain including the current node
        return current_max_gain
    
    get_max_gain(root)
    return max_path_sum

print(max_path(Node(value=8, children=(
            Node(value=10),
            Node(value=6, children=(
                Node(value=50),
                Node(value=10),
                Node(value=30, children=(
                    Node(value=15),
                    Node(value=10),
                ))
            )),
            Node(value=8, children=(
                Node(value=5),
                Node(value=5),
            )),
        ))))