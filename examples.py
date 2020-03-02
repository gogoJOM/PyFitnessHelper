from FHDataBase import FHProductsDataBase

def ProductsDBExample_SimpleCompanyProduct(a_DataBase):
    product_name = "gr"
    product_company = "Mi"
    key = a_DataBase.GetKey(product_name, product_company)

    calories = a_DataBase[key]

    if calories is None:
        new_calories = 220
        a_DataBase[key] = new_calories
    
    print(key, a_DataBase[key])

def ProductsDBExample_SimpleProduct(a_DataBase):
    product_name = "Beef"
    key = a_DataBase.GetKey(product_name)

    calories = a_DataBase[key]

    if calories is None:
        new_calories = 500
        a_DataBase[key] = new_calories
    
    print(key, a_DataBase[key])

if __name__ == "__main__":
    DataBase = FHProductsDataBase()
    ProductsDBExample_SimpleCompanyProduct(DataBase)
    ProductsDBExample_SimpleProduct(DataBase)
    print()
    