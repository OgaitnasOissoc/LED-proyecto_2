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
        self.isfunc = False
        self.isinyec = False
        self.issubyec = False
        self.isbiyec = False
    def rem_dupes(self):
        self.conections = list(dict.fromkeys(tuple(i) for i in self.conections))
        self.conections = [list(i) for i in self.conections]
    def add_conection(self,emiter,reciver,key):
        self.conections.append([emiter,key,reciver])
        self.rem_dupes()
    def check_func(self,emisores):
        domain = [x[0] for x in self.conections]
        domain.sort()
        if domain == emisores.users:
            self.isfunc = True
    def check_isinyec(self):
        ran = [x[2] for x in self.conections]
        nodupes = list(dict.fromkeys(ran))
        self.isinyec = False if len(nodupes) < len(ran) else True
    def check_issubyec(self,receptores):
        ran = [x[2] for x in self.conections]
        ran = list(dict.fromkeys(ran))
        ran.sort()
        if ran == receptores.users:
            self.issubyec = True
    def check_isbiyec(self):
        self.isbiyec = True if (self.isinyec == True) and (self.issubyec == True) else False
    def check_properties(self,emisores,receptores):
        self.check_func(emisores)
        self.check_isinyec()
        self.check_issubyec(receptores)
        self.check_isbiyec()


