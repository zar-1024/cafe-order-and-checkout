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

def get_bill(table_number):
    if table_number not in tables:
        print("This table is not occupied!")
        return 0
    return tables[table_number].get_bill()

def add_item(table_number, item):
    if table_number not in tables:
        tables[table_number] = Table([item])
    else:
        tables[table_number].add_item(item)

def add_items(table_number, items):
    for i in items:
        tables[table_number].add_item(i)

def remove_item(table_number, item):
    if table_number not in tables:
        print('This table is not occupied!')
    else:
        tables[table_number].remove