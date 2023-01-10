"""
Code for printing a binary tree nicely.

Chami Lamelas
Jan 2023
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def calculate_depth(root):
    """
    Calculates depth of tree of Nodes.

    Args:
        root: root of tree.

    Returns:
        The depth of tree.
    """
    return 0 if root is None else 1 + max(calculate_depth(root.left), calculate_depth(root.right))


def make_placeholder_tree(depth):
    """
    Makes fully balanced tree of Nodes with data = None that has provided depth.

    Args:
        depth: Depth of desired output tree.

    Returns:
        Root of constructed tree.
    """

    if depth == 0:
        return None
    root = Node(None)
    root.left = make_placeholder_tree(depth - 1)
    root.right = make_placeholder_tree(depth - 1)
    return root


def fill_tree_helper(root, depth):
    # Helper recursive function to fill_tree (on initial call assumes root is not None)
    # Put placeholder trees wherever we see a node with no child (base case)
    # Recursive case does copying of nodes from root

    if root is None:
        return make_placeholder_tree(depth)
    newroot = Node(root.data)
    newroot.left = fill_tree_helper(root.left, depth - 1)
    newroot.right = fill_tree_helper(root.right, depth - 1)
    return newroot


def fill_tree(root, depth):
    """
    Fills out tree with placeholder nodes (Node with data = None) and builds a fully balanced tree.

    Args:
        root: Original tree root.
        depth: Depth of tree rooted at root.

    Returns:
        Root of fully balanced tree with placeholder nodes.
    """
    return None if root is None else fill_tree_helper(root, depth)


def build_table(depth):
    """
    Builds index table to print a fully balanced tree of particular depth.

    An index table holds the indices for which we should try to print in print_table. For example depth 3 tree it
    looks like: [[3], [1,5], [0,2,4,6]]. For each row, you print at the indices, otherwise print some space.

    Args:
        depth: Depth for which we should build table.

    Returns:
        Index table.
    """
    nleaves = 2 ** (depth - 1)
    table = list()
    table.append([2 * i for i in range(nleaves)])
    for _ in range(depth - 1):
        curr = list()
        prev = table[-1]
        for i in range(0, len(prev), 2):
            curr.append(int((prev[i] + prev[i + 1]) / 2))
        table.append(curr)
    return table[::-1]


def level_order(root):
    """
    Builds level order traversal of data in tree rooted at root.

    Args:
        root: Root of tree.

    Returns:
        List with level order traversal of tree.
    """

    if root is None:
        return list()
    q = [root]
    out = list()
    while len(q) > 0:
        k = len(q)
        for _ in range(k):
            x = q.pop(0)
            if x.left is not None:
                q.append(x.left)
                q.append(x.right)
            out.append(x.data)
    return out


def print_table(root, table):
    """
    Prints index table constructed in build_table.

    Args:
        root: Tree to print using table.
        table: Index table.

    Returns:
        None
    """

    levelorder = level_order(root)
    level_idx = 0
    for row in table:
        row_idx = 0
        for i in range(row[-1] + 1):
            if i == row[row_idx]:
                print(' ' if levelorder[level_idx] is None else levelorder[level_idx], end='')
                row_idx += 1
                level_idx += 1
            else:
                # if data takes up more than 1 space, replace space with max data length and center str(data) in that
                # max data length spaces
                print(end=' ')
        print()


def print_tree(root):
    """
    Prints a tree rooted at root with spacing to show structure.

    For example, something like:

       1
         2
          3

    Args:
        root: Root of tree to print.

    Returns:
        None
    """

    depth = calculate_depth(root)
    filled_tree = fill_tree(root, depth)
    table = build_table(depth)
    print_table(filled_tree, table)


def main():
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    print_tree(root)


if __name__ == '__main__':
    main()
