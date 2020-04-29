from FHDataBase import FHProductsDataBase, FHPersonalDataBase
from utils import FHProduct, FHDay, SaveUsernames

def ProductsDBExample_SimpleCompanyProduct(a_DataBase):
    product_name = "gr"
    product_company = "Mi"

    key = a_DataBase.GetKey(product_name, product_company)

    calories = a_DataBase[key]

    if calories is None:
        new_calories = 220
        a_DataBase[key] = new_calories
    
    print(key, a_DataBase[key])
    print()

def ProductsDBExample_SimpleProduct(a_DataBase):
    product_name = "Beef"
    key = a_DataBase.GetKey(product_name)

    calories = a_DataBase[key]

    if calories is None:
        new_calories = 500
        a_DataBase[key] = new_calories

    product_name = "Beef eco"
    key = a_DataBase.GetKey(product_name)

    calories = a_DataBase[key]

    if calories is None:
        new_calories = 300
        a_DataBase[key] = new_calories
    
    print(key, a_DataBase[key])
    print()
   
def DayExample():
    day = FHDay("03.03.20", 80)

    breakfast = FHProduct("egg", None, 50)
    day.AddBreakfast(breakfast)

    first_snack = FHProduct("choco_bar", "Milka", 200)
    day.AddSnack(first_snack)

    lunch = FHProduct("salad", None, 100)
    day.AddLunch(lunch)
    lunch = FHProduct("Beef", None, 500)
    day.AddLunch(lunch)

    second_snack = FHProduct("jogurt", "Danone", 125)
    day.AddSnack(second_snack)

    dinner = FHProduct("steak", "Miratorg", 550)
    day.AddDinner(dinner)

    print(day)
    print()

    return day

def PersonalDBExample(a_DataBase, day):
    a_DataBase[day.date] = day
    
    a_DataBase.PrintInfo(day.date)

if __name__ == "__main__":
    DataBase = FHProductsDataBase()
    DataBase.Open()
    ProductsDBExample_SimpleCompanyProduct(DataBase)
    DataBase.Save()
    DataBase = FHProductsDataBase()
    DataBase.Open()
    ProductsDBExample_SimpleProduct(DataBase)
    DataBase.Save()
    day = DayExample()

    PersonalDB = FHPersonalDataBase("Anton")
    PersonalDB.Open()
    PersonalDBExample(PersonalDB, day)
    PersonalDB.Save()
    print()
    print(PersonalDB.keys())
    SaveUsernames(['Anton'])

    