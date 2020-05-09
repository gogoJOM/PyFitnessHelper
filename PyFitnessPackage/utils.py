import os


class FHProduct:
    def __init__(self, a_ProductName, a_Calories, a_ProductCompany=None):
        self.product_name = a_ProductName
        self.product_company = a_ProductCompany
        self.value = a_Calories

        if self.product_company is not None:
            self.key = a_ProductName + '_' + a_ProductCompany
        else:
            self.key = a_ProductName

    def __str__(self):
        return '{} ({})'.format(self.key, self.value)

    def __repr__(self):
        return str(self)


class FHDay:
    def __init__(self, a_Date=None, a_Weight=None):
        self.date = a_Date
        self.weight = a_Weight

        self.breakfast, self.lunch = [], []
        self.dinner, self.snacks = [], []
        self.breakfast_sum, self.lunch_sum = 0, 0
        self.dinner_sum, self.snacks_sum = 0, 0
        self.total = 0

        self.storage = {}

    def AddBreakfast(self, a_Product):
        # a_Product of type FHProduct
        self.breakfast.append(a_Product)
        self.breakfast_sum += a_Product.value
        self.total += a_Product.value

        if 'Breakfast' in self.storage.keys():
            self.storage['Breakfast'][a_Product] = a_Product.value
        else:
            self.storage['Breakfast'] = {a_Product: a_Product.value}

    def AddLunch(self, a_Product):
        # a_Product of type FHProduct
        self.lunch.append(a_Product)
        self.lunch_sum += a_Product.value
        self.total += a_Product.value

        if 'Lunch' in self.storage.keys():
            self.storage['Lunch'][a_Product] = a_Product.value
        else:
            self.storage['Lunch'] = {a_Product: a_Product.value}

    def AddDinner(self, a_Product):
        # a_Product of type FHProduct
        self.dinner.append(a_Product)
        self.dinner_sum += a_Product.value
        self.total += a_Product.value

        if 'Dinner' in self.storage.keys():
            self.storage['Dinner'][a_Product] = a_Product.value
        else:
            self.storage['Dinner'] = {a_Product: a_Product.value}

    def AddSnack(self, a_Product):
        # a_Product of type FHProduct
        self.snacks.append(a_Product)
        self.snacks_sum += a_Product.value
        self.total += a_Product.value

        if 'Snacks' in self.storage.keys():
            self.storage['Snacks'][a_Product] = a_Product.value
        else:
            self.storage['Snacks'] = {a_Product: a_Product.value}

    def SetWeight(self, a_Weight):
        self.weight = a_Weight

    def GetAll(self):
        return self.storage

    def __str__(self):
        return 'breakfast: {}, total: {}; \n\
lunch: {}, total: {}; \n\
dinner: {}, total: {}; \n\
snacks: {}, total: {}; \n\
TOTAL: {}.'.format(self.breakfast,
                   self.breakfast_sum,
                   self.lunch,
                   self.lunch_sum,
                   self.dinner,
                   self.dinner_sum,
                   self.snacks,
                   self.snacks_sum,
                   self.total)

    def __repr__(self):
        return str(self)


def LoadUsernames():
    try:
        with open('tmp/usernames.txt', 'r') as file:
            usernames = []
            for line in file:
                usernames.append(line.rstrip('\n'))
        return usernames
    except IOError:
        return []


def SaveUsernames(a_Usernames):
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    with open('tmp/usernames.txt', 'w') as file:
        for username in a_Usernames:
            file.write(username + '\n')


def PrintConsoleInfo():
    print('Welcome to FitnessHelper, console version.')
    print('If you would like to add information about \
            food you have eaten, type \'ADD\' and press Enter.')
    print('To stop adding type 0 and press Enter.')
    print('If you would like to see information about food \
            you have eaten at some date, type \'SHOW\' and press Enter.')
    print('If you would like to stop everything, type \'END\' \
            and press Enter.')


def PrintAddInfo():
    print('Your input string should be like:')
    print('<date (\'03.03.20\')> <breakfast (\'B\') / \
            lunch (\'L\') / snack (\'S\') / dinner (\'D\') > \
<product name> <product company> (optional) <calories for 100g> <weight>')


def PrintShowInfo():
    print('Your input string should be like:')
    print('<date (\'03.03.20\')> OR \'ALL\'')
