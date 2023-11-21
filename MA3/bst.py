""" bst.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""
import math
import random

from linked_list import LinkedList


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):  # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):  # Dicussed in the text on generators
        if self.root:
            yield from self.root

    # def insert(self, key):
    #     self.root = self._insert(self.root, key)
    #
    # def _insert(self, r, key):
    #     if r is None:
    #         return self.Node(key)
    #     elif key < r.key:
    #         r.left = self._insert(r.left, key)
    #     elif key > r.key:
    #         r.right = self._insert(r.right, key)
    #     else:
    #         pass  # Already there
    #     return r
    # Insert using iterative method
    def insert(self, key):
        if not self.root:
            self.root = self.Node(key)
            return
        r = self.root
        while True:
            if key < r.key:
                if r.left is None:
                    r.left = self.Node(key)
                    return
                r = r.left
            elif key > r.key:
                if r.right is None:
                    r.right = self.Node(key)
                    return
                r = r.right
            else:
                # Key already exists, no duplicates allowed
                return

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    # def contains(self, k):
    #     n = self.root
    #     while n and n.key != k:
    #         if k < n.key:
    #             n = n.left
    #         else:
    #             n = n.right
    #     return n is not None
    # Contains using recursion
    def contains(self, k):
        return self._contains(self.root, k)

    def _contains(self, r, k):
        # Doesn't exist
        if r is None:
            return
        if r.key == k:
            return r
        if k < r.key:
            r = self._contains(r.left, k)
        else:
            r = self._contains(r.right, k)
        return r

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    #
    #   Methods to be completed
    #

    def height(self):  # Compulsory
        return self._height(self.root)

    def _height(self, r):
        if r is None:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right))

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):  # Compulsory
        if r is None:
            return None
        elif k < r.key:
            # r.left = left subtree with k removed
            r.left = self._remove(r.left, k)
        elif k > r.key:
            # r.right =  right subtree with k removed
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:  # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            # Node has two children; find the inorder successor
            else:  # This is the tricky case.
                r.key = self._find_min(r.right).key
                r.right = self._remove(r.right, r.key)
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def _find_min(self, r):
        while r.left is not None:
            r = r.left
        return r

    def __str__(self):  # Compulsory
        elements = list(self.__iter__())
        elements_str = ', '.join(map(str, elements))
        return f"<{elements_str}>"

    # def to_list(self):                            # Compulsory
    #     return list(self.__iter__())
    def to_list(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, r, result):
        if r:
            self._inorder_traversal(r.left, result)
            result.append(r.key)
            self._inorder_traversal(r.right, result)

    def to_LinkedList(self):  # Compulsory
        linked_list = LinkedList()
        for i in self:
            linked_list.insert(i)
        return linked_list

    def ipl(self):  # Compulsory
        return self._ipl(self.root, 1)

    def _ipl(self, r, depth):
        if r is None:
            return 0
        return depth + self._ipl(r.left, depth + 1) + self._ipl(r.right, depth + 1)


def random_tree(n):  # Useful
    bst = BST()
    for _ in range(n):
        key = random.random()
        bst.insert(key)
    return bst


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")
    print(t.height())
    print(t.ipl())
    n = 1000
    print("n     theory  ipl/n  height")
    for i in range(5):
        tree = random_tree(n)
        print(n, round(1.39 * math.log(n, 2), 1), round(tree.ipl() / n, 1), tree.height(), sep="   ")
        n *= 2


if __name__ == "__main__":
    main()

"""
What is the generator good for?
==============================

1. computing size?
2. computing height?
3. contains?
4. insert?
5. remove?




Results for ipl of random trees
===============================
n      theory  ipl/n  height
1000   13.85   11.71   19
2000   15.24   14.37   28
4000   16.63   14.03   27
8000   18.02   15.65   29
16000  19.41   17.37   35

height will be logarithmic in 'n' on average



"""
