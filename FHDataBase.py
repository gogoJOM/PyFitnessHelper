class FHDataBase:
    def __init__(self):
        self.database = {}

    def __getitem__(self, key):
        if key in self.database:
            return self.database[key]
        return None    

    def __setitem__(self, key, value):
        self.database[key] = value

    def __contains__(self, item):
        return item in self.database

class FHProductsDataBase(FHDataBase):
    def GetKey(self, a_ProductName, a_ProductCompany=None):
        if a_ProductCompany is not None:
            return a_ProductName + '_' + a_ProductCompany
        return a_ProductName

class FHPersonalDataBase(FHDataBase):
    def PrintInfo(self, a_Date):
        print('====== {} ======'.format(a_Date))
        print(self[a_Date])

    def __str__(self):
        return str(self.database)

gProductDatabase = FHProductsDataBase()
gPersonalDatabase = FHPersonalDataBase()