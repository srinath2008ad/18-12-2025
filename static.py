class Animal:
    count = 0
    @staticmethod
    def animal(name):
        print(name)
        Animal.count += 1
        
Animal.animal("dog")
Animal.animal("cat")
Animal.animal("lion")
Animal.animal("cheetah")
print(Animal.count)