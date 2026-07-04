class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def to_dict(self):
        return {"name": self.name, "price": self.price, "qty": self.qty}
