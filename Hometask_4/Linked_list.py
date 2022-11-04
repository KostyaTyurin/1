class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())

class List:
    def __init__(self, array = None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

        if type(array) is list:
            for i in array:
                self.append(i)

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(
                Node(value, self._finish_pointer))

            prev_point = self._finish_pointer
            self._finish_pointer = Node(value, prev_point)
            self._finish_pointer.get_prev().set_next(self._finish_pointer)
            self._length += 1

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False
        if i <= len(self)/2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
        else:
            curr_pointer = self._finish_pointer
            for j in range(len(self) - i -1):
                curr_pointer = curr_pointer.get_prev()
        return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def pop(self, index):
        if (index < 0) or (index >= self._length):
            return False

        if (index <= len(self)/2):
            curr_pointer = self._start_pointer
            for j in range(index):
                curr_pointer = curr_pointer.get_next()
        else:
            curr_pointer = self._finish_pointer
            for j in range(len(self) - index - 1):
                curr_pointer = curr_pointer.get_prev()
        curr_pointer.get_prev().set_next(curr_pointer.get_next())
        curr_pointer.get_next().set_prev((curr_pointer.get_prev()))
        self._length -= 1
        return curr_pointer.get_value()

    def __add__(self, other):
        res = List()
        for i in range(len(self)):
            res.append(self[i])
        for j in range(len(other)):
            res.append(other[j])
        return res

    def __iter__(self):
        return StackIterator(self)


class StackIterator:
    def __init__(self, stack):
        self._stack = stack
        self._index = len(stack)

    def __next__(self):
        self._index -= 1
        res = self._stack[self._index]
        if self._index < 0:
            raise StopIteration
        return res


A = List([5, 34, 7, 9])
for a in A:
    print(a)
