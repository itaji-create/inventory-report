from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.count = 0

    def __next__(self):
        item = self.data[self.count]
        self.count += 1
        return item
