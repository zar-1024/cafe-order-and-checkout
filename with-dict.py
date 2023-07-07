from time import time

# items:
COFFEE, TEA, ICECREAM = 1, 2, 3

price = {
    COFFEE: 3000,
    TEA: 2500,
    ICECREAM: 6800
}

class Table:
    def __init__(self, items):
        self.last_active = time()
        print(self.last_active)
        self.items = items

    def get_idle_time(self):
        return time() - self.last_active

    def add_item(self, item):
        self.items.append(item)
        self.last_active = time()

    def remove_item(self, item):
        self.items.remove(item)

    def get_bill(self):
        result = 0
        for i in self.items:
            result += price[i]
        return result

tables = {
    1: Table([COFFEE, COFFEE, ICECREAM]),
    2: Table([]),
    3: Table([ICECREAM])
}

for t in tables:
    print(tables[t].get_bill())
