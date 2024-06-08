from oj import Node

def max_path(node: Node) -> int:
    res = [node.value]

    def dfs(root: Node) -> int:
        if not root:
            return 0
        child_vals: list[int] = []
        for child in root.children:
            child_vals.append(dfs(child))
        child_vals.sort(reverse=True)
        firstMax = child_vals[0] if len(child_vals) > 0 else 0
        secondMax = child_vals[1] if len(child_vals) > 1 else 0

        res[0] = max(res[0], root.value + firstMax + secondMax)
        return root.value + max(firstMax, secondMax)

    dfs(node)
    
    return res[0]

assert max_path(Node(value=8, children=(
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
        ))) == 101