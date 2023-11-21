""" linked_list.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""


class LinkedList:
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):  # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):  # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):  # Optional
        # Auxiliary method
        def _length(f):
            if f is None:
                return 0
            else:
                return 1 + _length(f.succ)

        return _length(self.first)

    def mean(self):  # Optional
        count = 0
        sum_ = 0
        f = self.first
        while f:
            count += 1
            sum_ += f.data
            f = f.succ
        return sum_ / count

    def remove_last(self):  # Optional
        # The linked list is empty
        if not self.first:
            raise ValueError("linkedlist is empty")
        # The linked list has only one element
        if not self.first.succ:
            val = self.first.data
            self.first = None
            return val
        f = self.first
        while f.succ.succ:
            f = f.succ
        val = f.succ.data
        f.succ = None
        return val

    def remove(self, x):  # Compulsory
        # The linked list is empty
        if not self.first:
            return False
        # x is the first element in the linked list
        if self.first.data == x:
            self.first = self.first.succ
            return True
        # Search in the rest of the linked list
        f = self.first
        while f.succ:
            if f.succ.data == x:
                f.succ = f.succ.succ
                return True
            f = f.succ
        return False

    def count(self, x):  # Optional
        def _count(x, f):
            if f is None:
                return 0
            if f.data == x:
                return 1 + _count(x, f.succ)
            else:
                return _count(x, f.succ)

        return _count(x, self.first)

    def to_list(self):  # Compulsory
        def _to_list(f):
            if f is None:
                return []
            else:
                return [f.data] + _to_list(f.succ)

        return _to_list(self.first)

    def remove_all(self, x):  # Compulsory
        def _remove_all(x, f):
            if f is None:
                return None, 0
            f.succ, count = _remove_all(x, f.succ)
            if f.data == x:
                return f.succ, count + 1
            else:
                return f, count

        self.first, count = _remove_all(x, self.first)
        return count

    def __str__(self):  # Compulsary
        values = list(self.__iter__())
        values_str = ', '.join(map(str, values))
        return f"({values_str})"

    def copy(self):  # Compulsory
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result

    ''' Complexity for this implementation: 
        Time Complexity = Theta(n)
        Space Complexity = Theta(n)
    '''

    def copy(self):  # Compulsary
        result = LinkedList()
        if self.first is None:
            return result
        current_original = self.first
        current_copy = LinkedList.Node(current_original.data, None)
        result.first = current_copy
        while current_original.succ:
            current_original = current_original.succ
            current_copy.succ = LinkedList.Node(current_original.data, None)
            current_copy = current_copy.succ
        return result

    ''' Complexity for this implementation:
        Time Complexity = Theta(n)
        Space Complexity = Theta(n)
    '''

    def __getitem__(self, ind):  # Compulsory
        # The linked list is empty
        if ind < 0:
            raise IndexError("Index must be non-negative")
        f = self.first
        i = 0
        while f:
            if i == ind:
                return f.data
            f = f.succ
            i += 1
        raise IndexError("Index out of range")


class Person:  # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.pnr == other.pnr

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.pnr < other.pnr
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Person):
            return self.pnr <= other.pnr
        return NotImplemented

    def __str__(self):
        return f"{self.name}:{self.pnr}"


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:
    print(lst.length())
    print(lst.remove_last())
    print(lst.to_list())
    print(lst.mean())
    print(lst.remove(1))
    print(lst.count(2))
    print(lst.remove_all(3))
    for x in lst:
        print(x, end=',')
    print()
    print(7 in lst)
    print(lst[3])
    x = lst.copy()
    print(x)

    # Exercise 11
    plist = []
    p = Person('Joby', 20)
    plist.insert(0, p)
    print(plist)
    q = Person('Anthony', 2)
    plist.insert(0, q)
    r = Person('Priya', 10)
    plist.insert(0, r)
    plist.sort()
    for i in plist:
        print(i)


if __name__ == '__main__':
    main()
