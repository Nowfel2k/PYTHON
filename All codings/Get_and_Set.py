class Patient:
    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setssn(self, ssn):
        self.ssn = ssn

    def getssn(self):
        return self.ssn

x = Patient()
x.setid(21)
x.setname('Mike Dane')
x.setssn(8035)
print(x.getid())
print(x.getname())
print(x.getssn())



