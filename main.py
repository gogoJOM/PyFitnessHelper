from FHDataBase import FHProductsDataBase, FHPersonalDataBase
from utils import PrintConsoleInfo, PrintAddInfo, FHProduct, FHDay

if __name__ == "__main__":
    type = 'console'
    # init DataBases
    gProductDatabase = FHProductsDataBase()
    gPersonalDatabase = FHPersonalDataBase()

    if type == 'console':
        PrintConsoleInfo()
        action = input()
        if action == 'ADD':
            # <date> <breakfast / lunch / snack / dinner> <product name> <product company> (optional) <calories for 100g> <weight>
            PrintAddInfo()
            while 1:
                adding = input().split(' ')
                if len(adding) == 1 and adding[0] == '0':
                    break
                if len(adding) < 5 or len(adding) > 6:
                    print('Incorrect len of input, read ADD instructions')
                
                date = adding[0]
                food_type = adding[1]
                product_name = adding[2]
                if len(adding) == 5:
                    product_company = None
                    calories_100 = float(adding[3])
                    weight = float(adding[4])
                else:
                    product_company = adding[3]
                    calories_100 = float(adding[4])
                    weight = float(adding[5])
                
                product = FHProduct(product_name, product_company, calories_100 * weight / 100)
                day = FHDay(date, gPersonalDatabase)
                
                if food_type == 'B':
                    day.AddBreakfast(product)
                elif food_type == 'L':
                    day.AddLunch(product)
                elif food_type == 'D':
                    day.AddDinner(product)
                elif food_type == 'S':
                    day.AddSnack(product)
                else:
                    print('Incorrect type of food, read ADD instructions')
                
                print(day)