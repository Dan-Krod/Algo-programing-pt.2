class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_diameter_of_binary_tree(tree):
    if not tree:
        return 0

    max_diameter = [0]

    def diameter_and_len_depth_of_binary_tree(tree):
        if not tree:
            return 0
        else:
            len_left_depth = diameter_and_len_depth_of_binary_tree(tree.left)
            len_right_depth = diameter_and_len_depth_of_binary_tree(tree.right)

            cur_diameter = len_right_depth + len_left_depth 
            if max_diameter[0] < cur_diameter:
                max_diameter[0] = cur_diameter

            if len_left_depth > len_right_depth:
                return len_left_depth + 1
            else:
                return len_right_depth + 1

    diameter_and_len_depth_of_binary_tree(tree)
    return max_diameter[0]
  
