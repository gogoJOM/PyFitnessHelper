import os
from utils import FHDay, FHProduct

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
                    line = line.rstrip('\n')
                    parts = line.split('|')
                    key, value = parts[0], parts[1]
                    self.database[key] = int(value)
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
            file.write('{} {}\n'.format(self.desired_kcal, self.desired_weight))
            for key in self.database.keys():
                file.write('{} | '.format(key))
				if 'Breakfast' in self.database[key].storage.keys():
                    for breakfast in self.database[key].storage['Breakfast'].keys():
                        file.write('{}_{}_{},'.format(breakfast.product_name, breakfast.product_company, breakfast.value))
                file.write(' | ')
				if 'Lunch' in self.database[key].storage.keys():
                    for breakfast in self.database[key].storage['Lunch'].keys():
                        file.write('{}_{}_{},'.format(breakfast.product_name, breakfast.product_company, breakfast.value))
                file.write(' | ')
				if 'Dinner' in self.database[key].storage.keys(): 
                    for breakfast in self.database[key].storage['Dinner'].keys():
                        file.write('{}_{}_{},'.format(breakfast.product_name, breakfast.product_company, breakfast.value))
                file.write(' | ')
				if 'Snacks' in self.database[key].storage.keys(): 
                    for breakfast in self.database[key].storage['Snacks'].keys():
                        file.write('{}_{}_{},'.format(breakfast.product_name, breakfast.product_company, breakfast.value))
                file.write(' | ')
                file.write('{} | {}\n'.format(self.database[key].total, self.database[key].weight))

    def Open(self):
        try:
            with open('tmp/{}.txt'.format(self.name), 'r') as file:

                for i, line in enumerate(file):
                    line = line.rstrip('\n')
                    if i == 0:
                        vls = line.split(' ')
                        self.desired_kcal, self.desired_weight = int(vls[0]), int(vls[1])
                        continue
                    parts = line.split(' | ')
                    key, breakfast, lunch, dinner, snacks, value, weight = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]
                    try:
                        weight = int(weight)
                    except:
                        weight = None
                    self.database[key] = FHDay(key, weight)

                    brkfst = breakfast.split(',')
                    for product in brkfst:
                        if len(product) > 0:
                            components = product.split('_')
                            name, company, calories = components[0], components[1], components[2]
                            if company == 'None':
                                company = None
                            self.database[key].AddBreakfast(FHProduct(name, int(calories), company))

                    brkfst = lunch.split(',')
                    for product in brkfst:
                        if len(product) > 0:
                            components = product.split('_')
                            name, company, calories = components[0], components[1], components[2]
                            if company == 'None':
                                company = None
                            self.database[key].AddLunch(FHProduct(name, int(calories), company))

                    brkfst = dinner.split(',')
                    for product in brkfst:
                        if len(product) > 0:
                            components = product.split('_')
                            name, company, calories = components[0], components[1], components[2]
                            if company == 'None':
                                company = None
                            self.database[key].AddDinner(FHProduct(name, int(calories), company))

                    brkfst = snacks.split(',')
                    for product in brkfst:
                        if len(product) > 0:
                            components = product.split('_')
                            name, company, calories = components[0], components[1], components[2]
                            if company == 'None':
                                company = None
                            self.database[key].AddSnack(FHProduct(name, int(calories), company))

                    self.database[key].total = float(value)
                    # self.database[key].weight = weight
        except IOError:
            print("Making new personal database for {}".format(self.name))

gProductDatabase = FHProductsDataBase()
gPersonalDatabase = FHPersonalDataBase("username")