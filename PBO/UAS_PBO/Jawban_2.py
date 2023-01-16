class tumbuhan:
    def __init__(self):
        self.anggrek = "Anggrek"
        self.mawar = "Mawar"
        self.melati = "Melati"
        

class garden:
    def __init__(self):
        tumbuhan.__init__(self)
        print(self.__mawar)
        print ("call class garden")
        
obj = tumbuhan()
print(obj.melati)
print(obj.anggrek)
print(obj.mawar)