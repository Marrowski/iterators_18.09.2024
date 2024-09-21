class NewIterator:
    def __init__(self, list_iter: list):
        self.list_iter = list_iter

    def __iter__(self):
        return self

    def __next__(self):
        value = self.list_iter[::-1]
        return value


iterator = NewIterator([1, 2, 3, 4, 5, 6, 7])

for i in iterator:
    print(i)
    break