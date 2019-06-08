

while(False):
    print("aaaa")


def add(a=1, b=2):
    return a + b

count = add()
print(count)

class Person():
    def __init__(self, username="person"):
        self.username = username
    
    def eat(self):
        print("人能吃饭")
    
    def run(self):
        print("人能跑路")
    
class Son(Person):
    pass

huangshuang = Person()
print(huangshuang.username)

hs = Person("huangshuang")
print(hs.username)

hs.eat()
hs.run()

son = Son()
son.run()
son.eat()
print(son.username)