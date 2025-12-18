class Animal:
    count = 0
    def __init__(self, name):
        self.name = name
        Animal.count += 1
    def show(self):
        print(self.name)
        
a = Animal("dog")
b = Animal("cat")
c = Animal("lion")
d = Animal("cheetah")
a.show()
b.show()
c.show()
d.show()
print(Animal.count)