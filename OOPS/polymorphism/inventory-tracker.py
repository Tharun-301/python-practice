from collections import UserDict

class Inventory(UserDict):
    def __init__(self):
        super().__init__()

    def __setitem__(self, item, qty):
        if not isinstance(item, str) or not isinstance(qty, int):
            raise Exception('Product: Quantity should be string:integer')
        super().__setitem__(item.lower(), qty)

    def __getitem__(self, item):
        return super().__getitem__(item.lower())

    def __delitem__(self, item):
        return super().__delitem__(item.lower())

    def __contains__(self, item):
        return super().__contains__(item.lower())

    def update_stock(self, item, qty):
        if item in self:
            self[item] += qty
        else:
            self[item] = qty


inventory = Inventory()
inventory['Apple'] = 10
inventory['banana'] = 15
inventory.update_stock('apple', -1)
print(inventory['APPle'])