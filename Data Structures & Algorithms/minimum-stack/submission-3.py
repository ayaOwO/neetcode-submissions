class MinStack:
    def __init__(self):
        self._stack = []
        self._length = 0
        self._mins = []

    def push(self, val: int) -> None:
        self._stack.append(val)

        # update minimum stack
        if self._length > 0:
            min_val = min(self._mins[-1], val)
        else:
            min_val = val

        self._mins.append(min_val)

        self._length += 1

    def pop(self) -> None:
        if self._length < 1:
            return
        del self._stack[self._length - 1]
        del self._mins[self._length - 1]
        self._length -= 1
        self._length = max(self._length, 0)

    def top(self) -> int | None:
        return self._stack[self._length - 1]

    def getMin(self) -> int | None:
        return self._mins[self._length - 1]
