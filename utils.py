class FHProduct:
    def __init__(self, a_ProductName, a_ProductCompany, a_Calories):
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
    def __init__(self, a_Date, a_ProductBase): 
        self.date = a_Date
        self.database = a_ProductBase

        self.breakfast, self.lunch = [], []
        self.dinner, self.snacks = [], []
        self.breakfast_sum, self.lunch_sum = 0, 0
        self.dinner_sum, self.snacks_sum = 0, 0

    def AddBreakfast(self, a_Product):
        # a_Product of type FHProduct
        self.breakfast.append(a_Product)
        self.breakfast_sum += a_Product.value

    def AddLunch(self, a_Product):
        # a_Product of type FHProduct
        self.lunch.append(a_Product)
        self.lunch_sum += a_Product.value

    def AddDinner(self, a_Product):
        # a_Product of type FHProduct
        self.dinner.append(a_Product)
        self.dinner_sum += a_Product.value

    def AddSnack(self, a_Product):
        # a_Product of type FHProduct
        self.snacks.append(a_Product)
        self.snacks_sum += a_Product.value

    def __str__(self):
        return 'breakfast: {}, total: {}; \n\
lunch: {}, total: {}; \n\
dinner: {}, total: {}; \n\
snacks: {}, total: {};'.format(self.breakfast, self.breakfast_sum,
                self.lunch, self.lunch_sum, self.dinner, self.dinner_sum,
                self.snacks, self.snacks_sum)