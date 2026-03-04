import random

class Set:
    set = []

    def userset(self, x):
        self.set = x

    def addset(self,x):
        self.user.extend(x)

    def randset(self, x):
        match x:
            case 1:
                length = random.randint(0,30)
                for _ in range(length):
                    self.set.append(random.randint(1,100))
            
            case 2:
                length = random.randint(0,15)
                for _ in range(length):
                    self.set.append(chr(random.randint(33,126)))


