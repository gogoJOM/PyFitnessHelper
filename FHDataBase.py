class FHDataBase:
    def __init__(self):
        self.database = {}

class FHProductsDataBase(FHDataBase):
    def __init__(self):
        super().__init__()
        # { product_name + '_' + product_company : calories }
    
    def __getitem__(self, key):
        if key in self.database:
            return self.database[key]
        return None    

    def __setitem__(self, key, value):
        self.database[key] = value

    def GetKey(self, a_ProductName, a_ProductCompany=None):
        if a_ProductCompany is not None:
            return a_ProductName + '_' + a_ProductCompany
        return a_ProductName