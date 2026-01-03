class Item:
    def __init__(self, id, name, price, purcahse_price):
        self.id = id
        self.name = name
        self.price = price
        self.purcahse_price = purcahse_price
    
    def genka(self):
        result = self.purcahse_price / self.price
        return result
    
item_1 = Item("A0001", "Tシャツ", 5000, 2250)
print(item_1.genka())