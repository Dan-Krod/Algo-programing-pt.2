class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1


class AVLTree_Priority_Queue:
    def __init__(self):
        self.root = None

    def get_height(self, cur_node):
        if cur_node is not None:
            return cur_node.height
        else:
            return 0

    def insert(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
        else:
            self._insert_recursion_and_dfs(value, self.root, priority)

    def _insert_recursion_and_dfs(self, value, insert_node, priority):
        if not insert_node:
            return Node(value, priority)

        if priority >= insert_node.priority:
            if insert_node.left is None:
                insert_node.left = Node(value, priority)
                insert_node.left.parent = insert_node
                self._balance_after_insertion(insert_node.left)
                return insert_node.left
            else:
                return self._insert_recursion_and_dfs(value, insert_node.left, priority)

        if priority < insert_node.priority:
            if insert_node.right is None:
                insert_node.right = Node(value, priority)
                insert_node.right.parent = insert_node
                self._balance_after_insertion(insert_node.right)
                return insert_node.right
            else:
                return self._insert_recursion_and_dfs(
                    value, insert_node.right, priority
                )

    def _balance_after_insertion(self, cur_node):
        if cur_node is None:
            return
        balance = self.get_height(cur_node.left) - self.get_height(cur_node.right)

        if abs(balance) > 1:
            self._main_balance_of_tree(cur_node)
        if cur_node.parent is not None:
            self._balance_after_insertion(cur_node.parent)

    def _main_balance_of_tree(self, cur_node):
        if cur_node is None:
            return

        balance = self.get_height(cur_node.left) - self.get_height(cur_node.right)

        if balance > 1:
            if cur_node.left and cur_node.left.priority < cur_node.priority:
                cur_node.left = self.left_rotate(cur_node.left)
                return self.right_rotate(cur_node)
            elif cur_node.left and cur_node.left.priority >= cur_node.priority:
                self.right_rotate(cur_node)

        if balance < -1:
            if cur_node.right and cur_node.right.priority >= cur_node.priority:
                cur_node.right = self.right_rotate(cur_node.right)
                return self.left_rotate(cur_node)
            elif cur_node.right and cur_node.right.priority < cur_node.priority:
                return self.left_rotate(cur_node)

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root
        new_root.left = node
        node.parent = new_root
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(
            self.get_height(new_root.left), self.get_height(new_root.right)
        )

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = node
        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
        new_root.right = node
        node.parent = new_root
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(
            self.get_height(new_root.left), self.get_height(new_root.right)
        )

    def remove_highest_priority_node(self):
        if self.root is None:
            return None

        current = self.root
        while current.right:
            current = current.right

        value = current.value
        self._delete_node(current.parent, current.priority)
        return value

    def _delete_node(self, root, priority):
        if not root:
            return
        if priority < root.priority:
            root.left = self._delete_node(root.left, priority)
        elif priority > root.priority:
            root.right = self._delete_node(root.right, priority)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._find_highest_priority_node(root.right)
            root.value = temp.value
            root.priority = temp.priority
            root.right = self._delete_node(root.right, temp.priority)

        return self._main_balance_of_tree(root)

    def _find_highest_priority_node(self, node):
        if node.right:
            return self._find_highest_priority_node(node.right, node)
        return node

    def view_priority_queue(self):
        if self.root is None:
            return []

        queue = []
        self.inorder_traversal(self.root, queue)
        return queue

    def inorder_traversal(self, node, queue):
        if node is None:
            return
        self.inorder_traversal(node.left, queue)
        queue.append((node.value, node.priority))
        self.inorder_traversal(node.right, queue)

    def peek(self):
        return self.root.value if self.root else None
