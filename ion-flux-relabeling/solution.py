def is_q_node_in_range(q_node, tree):
    return (q_node < 1) or (q_node >= tree[-1])


def search_tree(tree, parent, q_node):
    # recusrion end
    if (tree[-1] == q_node) or is_q_node_in_range(q_node, tree):
        return parent
    
    # tree indexes
    len_tree = len(tree)
    tree_middle_ix = int((len_tree - 1)/2)

    # search subtrees
    if tree[tree_middle_ix - 1]>=q_node:
        # search left tree
        return search_tree(tree=tree[:tree_middle_ix], parent=tree[-1], q_node=q_node)
    else:
        # search right tree
        return search_tree(tree=tree[tree_middle_ix:-1], parent=tree[-1], q_node=q_node)


def solution(h, q):
    # input tree
    tree_post_order_traversal = [node for node in range(1, 2**h)]

    # default parent val
    default_parent = -1

    # solution
    solution = [search_tree(tree=tree_post_order_traversal, parent=default_parent, q_node=q_node) for q_node in q]

    return solution


if __name__ == "__main__":
    assert solution(3, [7, 3, 5, 1]) == [-1, 7, 6, 3]
    assert solution(5, [19, 14, 28]) == [21, 15, 29]
