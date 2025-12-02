class Company():
    def __init__(self):
        # self.companyname = "Infosys"    # public
        # self.__companyname = "Infosys"    # private
        self._companyname = "Infosys"     # protected

    # def companyName(self):
    #     print(self.__companyname)

c1 = Company()
# c1.companyname = "Google"
# c1.companyName()
print(c1._companyname)


print("derived class")
class b(Company):
    pass

b1 = b()
print(b1._companyname)


# self.companyname ===> public
# self.__companyname ===> private
# self._comapnyname ===> protected



