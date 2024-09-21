class MyIterator:
    def __init__(self, num_first: int, num_end: int):
        self.num_first = num_first
        self.num_end = num_end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_first < self.num_end:
            value = self.num_first
            self.num_first += 1
            return value
        else:
            raise StopIteration


new_iter = MyIterator(1, 10)
for num in new_iter:
    print(num)