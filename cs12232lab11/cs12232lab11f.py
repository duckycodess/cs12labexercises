from oj import Node

def max_path(node: Node) -> int:
    answer = [node.value]

    def find_path(root: Node) -> int:
        if not root:
            return 0
        child_vals: list[int] = []
        for child in root.children:
            child_vals.append(find_path(child))
        child_vals.sort(reverse=True)
        firstMax = child_vals[0] if len(child_vals) > 0 else 0
        secondMax = child_vals[1] if len(child_vals) > 1 else 0

        answer[0] = max(answer[0], root.value + firstMax + secondMax)
        return root.value + max(firstMax, secondMax)

    find_path(node)
    
    return answer[0]