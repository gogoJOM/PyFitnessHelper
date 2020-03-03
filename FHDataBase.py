class FHDataBase:
    def __init__(self):
        self.database = {}

    def __getitem__(self, key):
        if key in self.database:
            return self.database[key]
        return None    

    def __setitem__(self, key, value):
        self.database[key] = value

class FHProductsDataBase(FHDataBase):
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(FHProductsDataBase, self).__new__(self)
        return self.instance

    def GetKey(self, a_ProductName, a_ProductCompany=None):
        if a_ProductCompany is not None:
            return a_ProductName + '_' + a_ProductCompany
        return a_ProductName

class FHPersonalDataBase(FHDataBase):
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(FHDataBase, self).__new__(self)
        return self.instance

    def PrintInfo(self, a_Date):
        print('====== {} ======'.format(a_Date))
        print(self[a_Date])