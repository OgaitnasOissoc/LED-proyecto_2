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
    def prop_funciones(self):
    def add_conection(self,emiter,reciver,key):
        self.conections.append([emiter,key,reciver])
        self.rem_dupes()
    def check_properties(self,emisores,receptores):


