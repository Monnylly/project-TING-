class Queue:
    def __init__(self):
        self._head_value = list()

    def __len__(self):
        return len(self._head_value)

    def enqueue(self, value):
        self._head_value.append(value)

    def dequeue(self):
        if not self.__len__():
            return None

        result_last = self._head_value[0]
        del self._head_value[0]
        return result_last

    def search(self, index):
        result = self.__len__() + 1
        if result < index or index < 0:
            raise IndexError
        return self._head_value[index]
