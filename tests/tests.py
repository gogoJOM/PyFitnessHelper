try:
    from PyFitnessPackage.utils import FHDay, FHProduct
    from PyFitnessPackage.FHDataBase import FHProductsDataBase, FHPersonalDataBase
except:
    import sys
    sys.path.append('PyFitnessPackage/')
    from utils import FHDay, FHProduct
    from FHDataBase import FHProductsDataBase, FHPersonalDataBase


def test_FHProduct_nocompany():
    product = FHProduct("SomeProduct", 99)

    assert product.key == "SomeProduct"
    assert product.value == 99

    str_representation = str(product)

    assert str_representation == "SomeProduct (99)"


def test_FHProduct_normal():
    product = FHProduct("SomeProduct", 99, "SomeCompany")

    assert product.key == "SomeProduct_SomeCompany"
    assert product.value == 99

    str_representation = str(product)

    assert str_representation == "SomeProduct_SomeCompany (99)"


def test_FHDay_breakfast():
    day = FHDay("10.10.2010", 200)

    assert day.date == "10.10.2010"
    assert day.weight == 200
    assert day.total == 0

    product = FHProduct("BProduct", 20)

    day.AddBreakfast(product)

    assert day.breakfast_sum == 20
    assert len(day.breakfast) == 1
    assert str(day.breakfast[0]) == 'BProduct (20)'
    assert day.total == 20

    product = FHProduct("B2Product", 30)

    day.AddBreakfast(product)

    assert day.breakfast_sum == 50
    assert len(day.breakfast) == 2
    assert str(day.breakfast[0]) == 'BProduct (20)'
    assert str(day.breakfast[1]) == 'B2Product (30)'
    assert day.total == 50


def test_FHDay_lunch():
    day = FHDay("10.10.2010", 200)

    assert day.date == "10.10.2010"
    assert day.weight == 200
    assert day.total == 0

    product = FHProduct("LProduct", 40)

    day.AddLunch(product)

    assert day.lunch_sum == 40
    assert len(day.lunch) == 1
    assert str(day.lunch[0]) == 'LProduct (40)'
    assert day.total == 40

    product = FHProduct("L2Product", 50)

    day.AddLunch(product)

    assert day.lunch_sum == 90
    assert len(day.lunch) == 2
    assert str(day.lunch[0]) == 'LProduct (40)'
    assert str(day.lunch[1]) == 'L2Product (50)'
    assert day.total == 90


def test_FHDay_dinner():
    day = FHDay("10.10.2010", 200)

    assert day.date == "10.10.2010"
    assert day.weight == 200
    assert day.total == 0

    product = FHProduct("DProduct", 120)

    day.AddDinner(product)

    assert day.dinner_sum == 120
    assert len(day.dinner) == 1
    assert str(day.dinner[0]) == 'DProduct (120)'
    assert day.total == 120

    product = FHProduct("D2Product", 130)

    day.AddDinner(product)

    assert day.dinner_sum == 250
    assert len(day.dinner) == 2
    assert str(day.dinner[0]) == 'DProduct (120)'
    assert str(day.dinner[1]) == 'D2Product (130)'
    assert day.total == 250


def test_FHDay_snack():
    day = FHDay("10.10.2010", 200)

    assert day.date == "10.10.2010"
    assert day.weight == 200
    assert day.total == 0

    product = FHProduct("SProduct", 220)

    day.AddSnack(product)

    assert day.snacks_sum == 220
    assert len(day.snacks) == 1
    assert str(day.snacks[0]) == 'SProduct (220)'
    assert day.total == 220

    product = FHProduct("S2Product", 230)

    day.AddSnack(product)

    assert day.snacks_sum == 450
    assert len(day.snacks) == 2
    assert str(day.snacks[0]) == 'SProduct (220)'
    assert str(day.snacks[1]) == 'S2Product (230)'
    assert day.total == 450


def test_FHDay_full():
    day = FHDay("10.10.2010", 200)

    assert day.date == "10.10.2010"
    assert day.weight == 200
    assert day.total == 0

    product = FHProduct("BProduct", 20)

    day.AddBreakfast(product)

    assert day.breakfast_sum == 20
    assert len(day.breakfast) == 1
    assert str(day.breakfast[0]) == 'BProduct (20)'
    assert day.total == 20

    product = FHProduct("LProduct", 40)

    day.AddLunch(product)

    assert day.breakfast_sum == 20
    assert day.lunch_sum == 40
    assert len(day.lunch) == 1
    assert len(day.breakfast) == 1
    assert str(day.lunch[0]) == 'LProduct (40)'
    assert str(day.breakfast[0]) == 'BProduct (20)'
    assert day.total == 60

    product = FHProduct("DProduct", 120)

    day.AddDinner(product)

    assert day.dinner_sum == 120
    assert day.breakfast_sum == 20
    assert day.lunch_sum == 40
    assert len(day.dinner) == 1
    assert len(day.lunch) == 1
    assert len(day.breakfast) == 1
    assert str(day.dinner[0]) == 'DProduct (120)'
    assert str(day.lunch[0]) == 'LProduct (40)'
    assert str(day.breakfast[0]) == 'BProduct (20)'
    assert day.total == 180

    product = FHProduct("SProduct", 220)

    day.AddSnack(product)
    assert day.dinner_sum == 120
    assert day.breakfast_sum == 20
    assert day.lunch_sum == 40
    assert day.snacks_sum == 220
    assert len(day.dinner) == 1
    assert len(day.lunch) == 1
    assert len(day.breakfast) == 1
    assert len(day.snacks) == 1
    assert str(day.dinner[0]) == 'DProduct (120)'
    assert str(day.lunch[0]) == 'LProduct (40)'
    assert str(day.breakfast[0]) == 'BProduct (20)'
    assert str(day.snacks[0]) == 'SProduct (220)'
    assert day.total == 400

    storage = day.GetAll()
    keys = list(storage.keys())
    assert len(keys) == 4

    key_breakfast = list(storage['Breakfast'].keys())
    assert len(key_breakfast) == 1
    assert str(key_breakfast[0]) == 'BProduct (20)'
    assert storage['Breakfast'][key_breakfast[0]] == 20


def test_FHProductsDataBase():
    base = FHProductsDataBase()

    product_name, product_company = "Product", "Company"
    key = base.GetKey(product_name, product_company)

    assert key == "Product_Company"

    calories = base[key]

    assert calories is None

    if calories is None:
        new_calories = 500
        base[key] = new_calories

    assert base[key] == 500

    product_name, product_company = "Product2", "Company2"
    key = base.GetKey(product_name, product_company)

    assert key == "Product2_Company2"

    base[key] = 600
    keys = list(base.keys())

    assert len(keys) == 2
    assert ('Product_Company' in keys) is True
    assert ('Product2_Company2' in keys) is True


def test_FHPersonalDataBase():
    base = FHPersonalDataBase("TestName", 2000, 80)

    assert base.name == "TestName"
    assert base.desired_kcal == 2000
    assert base.desired_weight == 80

    day = FHDay("10.10.2010", 200)

    product = FHProduct("BProduct", 20)
    day.AddBreakfast(product)

    product = FHProduct("LProduct", 40)
    day.AddLunch(product)

    product = FHProduct("DProduct", 120)
    day.AddDinner(product)

    product = FHProduct("SProduct", 220)
    day.AddSnack(product)

    base[day.date] = day

    assert base[day.date].total == 400
