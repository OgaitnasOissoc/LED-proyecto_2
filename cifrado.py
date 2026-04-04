from set import Set

class Participant:
    def __init__(self,users):
        self.users = users
    def add_user(self,x):
        self.users.append(x)
        self.users.sort()
    def remove_user(self,x):
        self.users.remove(x)
        self.users.sort()
class Conection:
    def __init__(self,conections):
        self.conections = conections
        self.relation = []
        self.isfunc = False
        self.isinyec = False
        self.issubyec = False
        self.isbiyec = False
        self.isreflex = False
        self.issimet = False
        self.istrans = False
    def rem_dupes(self):
        self.conections = list(dict.fromkeys(tuple(i) for i in self.conections))
        self.conections = [list(i) for i in self.conections]
    def add_conection(self,emiter,reciver,key):
        self.conections.append([emiter,key,reciver])
        self.rem_dupes()
    def check_func(self,emisores):
        domain = [x[0] for x in self.conections]
        for i in emisores.users:
            if domain.count(i) != 1:
                self.isfunc = False
                return
        self.isfunc = True
    def check_isinyec(self):
        ran = [x[2] for x in self.conections]
        for i in ran:
            if ran.count(i) != 1:
                self.isinyec = False
                return
        self.isinyec = True
    def check_issubyec(self,receptores):
        ran = [x[2] for x in self.conections]
        for i in receptores.users:
            if i not in ran:
                self.issubyec = False
                return
        self.issubyec = True
    def check_isbiyec(self):
        self.isbiyec = True if (self.isinyec == True) and (self.issubyec == True) else False
    def check_properties(self,emisores,receptores):
        self.check_func(emisores)
        self.check_isinyec()
        self.check_issubyec(receptores)
        self.check_isbiyec()
    def make_relation(self):
        self.relation = [(x[0],x[2]) for x in self.conections]
    def check_isreflex(self):
        self.isreflex = True
        for i in self.conections:
            if (i[0],i[0]) not in self.relation:
                self.isreflex = False
                break
    def check_issimet(self):
        self.issimet = True
        for i in self.relation:
            if (i[1],i[0]) not in self.relation:
                self.issimet = False
                break
    def check_istrans(self):
        self.istrans = True
        for i in self.relation:
            for j in self.relation:
                if (i[1] == j[0]) and (i[0],j[1]) not in self.relation :
                    self.istrans = False
                    return
    def check_properties_relation(self):
        self.check_isreflex()
        self.check_issimet()
        self.check_istrans()


