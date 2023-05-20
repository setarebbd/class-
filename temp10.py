class Cmputer:
    count = 0

    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram+self.hard+self.cpu


aaaaaaaaaaaaaaaaaaaa


class Laptop(Cmputer):
    def value(self):
        return self.ram+self.hard+self.cpu+self.size


pc1 = Cmputer(12, 2, 4)
pc2 = Cmputer(8, 4, 6)
print(pc1.value())
print(pc2.value())
laptop1 = Laptop(16, 2, 4,)
laptop1.size = 13
print(laptop1.value())
