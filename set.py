import random

class Set:

    def __init__(self,isuni):
        self.isuni = isuni
        self.set = []       
    def remove_dupes(self, factors):
        return list(dict.fromkeys(factors))

    def userset(self, x):
        self.set = self.remove_dupes(x)

    def addset(self,x):
        self.set.extend(x)

    def randset(self, x):
        match x:
            case 0:
                length = random.randint(0,30)
                for _ in range(length):
                    self.set.append(random.randint(1,100))
            
            case 1:
                length = random.randint(0,15)
                for _ in range(length):
                    self.set.append(chr(random.randint(33,126)))
    def syncuni(self, x):
        for i in x:
            if i not in self.set:
                self.set.append(i)
    def union(self, conjunto2):
        union = self.remove_dupes((self.set + conjunto2))
        return union
    def interseccion(self,conjunto2):
        interseccion = []
        for i in self.set:
            if i in conjunto2:
                interseccion.append(i)
        interseccion = self.remove_dupes(interseccion)
        return interseccion
    def diferencia(self,conjunto2):
        diferencia = self.set.copy()
        for i in conjunto2:
            if i in diferencia:
                diferencia.remove(i)
        return diferencia
    def diferencia_simetrica(self,conjunto2):
        diferencia = self.remove_dupes((self.set + conjunto2))
        for i in self.set:
            if i in conjunto2:
                diferencia.remove(i)
        return diferencia
    def complemento(self, universo):
        complemento = universo.copy()
        for i in self.set:
            if i in complemento:
                complemento.remove(i)
        return complemento
    def igualdad(self,conjunto2):
        return True if self.set == conjunto2 else False
    def subconjunto(self, conjunto2):
        flag = True
        for i in self.set:
            if i not in conjunto2:
                flag = False
                break
        return flag
    def subconjunto_propio(self, conjunto2):
        return False if self.igualdad(conjunto2) == True else self.subconjunto(conjunto2)
    def disjunto(self,conjunto2):
        flag = True
        for i in self.set:
            if i in conjunto2:
                flag = False
                break
        return flag
