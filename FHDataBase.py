import os
from utils import FHDay

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

    def keys(self):
        return self.database.keys()

class FHProductsDataBase(FHDataBase):
    def GetKey(self, a_ProductName, a_ProductCompany=None):
        if a_ProductCompany is not None:
            return a_ProductName + '_' + a_ProductCompany
        return a_ProductName

    def Save(self):
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        with open('tmp/productbase.txt', 'w') as file:
            for key in self.database.keys():
                file.write('{}|{}\n'.format(key, self.database[key]))

    def Open(self):
        try:
            with open('tmp/productbase.txt', 'r') as file:
                for line in file:
                    parts = line.split('|')
                    key, value = parts[0], parts[1]
                    self.database[key] = value
        except IOError:
            print("Making new product database")

class FHPersonalDataBase(FHDataBase):
    def __init__(self, name, desired_kcal=1000, desired_weight=100):
        FHDataBase.__init__(self)
        self.name = name
        self.desired_kcal = desired_kcal
        self.desired_weight = desired_weight 

    def PrintInfo(self, a_Date):
        print('====== {} ======'.format(a_Date))
        print(self[a_Date])

    def __str__(self):
        return str(self.database)

    def Save(self):
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        with open('tmp/{}.txt'.format(self.name), 'w') as file:
            for key in self.database.keys():
                file.write('{} | {}\n'.format(key, self.database[key].total))

    def Open(self):
        try:
            with open('tmp/{}.txt'.format(self.name), 'r') as file:
                for line in file:
                    parts = line.split(' | ')
                    key, value = parts[0], parts[1]
                    self.database[key] = FHDay(key)
                    self.database[key].total = value
        except IOError:
            print("Making new personal database for {}".format(self.name))

gProductDatabase = FHProductsDataBase()
gPersonalDatabase = FHPersonalDataBase("username")