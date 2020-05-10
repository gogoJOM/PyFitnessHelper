# Проект Fitness Helper

Выполненный проект представляет собой приложение, позволяющее пользователю вести подсчёт употребляемого количества килокаллорий в день и запись текущего веса.

**Содержание**
- [Установка](#setting)
  - [Сборка пакета](#package)
  - [Запуск исходного файла](#clone)
  - [Сборка документации](#documentation)
- [Выбор пользователя](#create_user)
  - [Создание нового пользователя](#new_user)
  - [Выбор уже существуещего пользователя](#choose_user)
- [Таблица с информацией](#table)
  - [Добавление продукта в текущий день](#add_product)
  - [Создание нового продукта](#new_product)
  - [Информация о предыдущих днях](#day_info)
- [Сохренение](#save)


## Установка <a name="setting"></a>

### Сборка пакета <a name="package"></a>

Чтобы собрать package на python достаточно воспользоваться командой (понадобятся setuptools и wheel):

```
python setup.py bdist_wheel
```

Далее можно через pip ставить созданный whl файл.


Для запуска проекта (если он установлен как package) нужны комманды:

```
import PyFitnessPackage.run_app
PyFitnessPackage.run_app.run_helper()
```

### Запуск исходного файла <a name="clone"></a>

Либо можно скопировать репозиторий:

```
git clone https://github.com/gogoJOM/PyFitnessHelper
```

Если запуск происходит под Windows, нужно установить необходимые пакеты:

```
pip install -r requirements.txt
```

Затем, чтобы запустить приложение, достаточно следующей команды:

```
python main.py
```

### Сборка документации <a name="documentation"></a>

Если скачать папку sdoc, можно собрать документацию следующим образом:

```
cd sdoc
make html
```

Результат окажется в папке ```sdoc/build/html```

## Выбор пользователя <a name="create_user"></a>

При запуске приложения пользователю предлагается выбрать аккаунт, существует 2 возможности:

### Создание нового пользователя <a name="new_user"></a>

Для этого нужно заполнить все поля таблицы в левом верхнем углу окна и нажать кнопку "Create new user".

![](https://github.com/gogoJOM/PyFitnessHelper/sdoc/source/_static/new_user_info.png "Create new user")

Если пользователь с таким именем существует, приложение выдаст информацию об ошибке:

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/warning_username.png "Error message")

Так же ошибка может возникнуть, если какое-либо поле при создании пользователя не было заполнено:

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/warning_weight.png "Error message")

### Выбор уже существуещего пользователя <a name="choose_user"></a>

Если пользователь уже пользовался приложением, он может выбрать свой аккаунт и нажать кнопку "Choose user".

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/choose_user.png "Choose user")

Если пользователь не был выбран (остался "New"), а кнопка нажата, пользователь опять получит информацию об ошибке.

## Таблица с информацией <a name="table"></a>

Сразу после выбора/создания пользователя, загружаются поля с информацией по текущему дню и функционалом по добавлению новой информации.
По умолчанию день выбран как текущий.

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/day_info1.png "Day info")

### Добавление продукта в текущий день <a name="add_product"></a>

Для того, чтобы добавить новый продукт, пользователь может выбрать время приёма пищи:

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/add_product1.png "Add product")

Затем выбрать продукт из уже существующих в базе данных:

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/add_product2.png "Add product")

Ввести употреблённое количество и нажать кнопку "Add":

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/add_product3.png "Add product")

После чего таблица с информацией автоматически обновится:

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/add_product4.png "Add product")

### Создание нового продукта <a name="new_product"></a>

Если нужного продукта или блюда не существует в базе, пользователь может его создать. Для этого нужно выбрать продукт как "New" и нажать кнопку "Add". В результате чего появится окно, куда можно ввести данные о новом продукте.

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/new_product1.png "New product")

После того, как пользователь ввёл информацию о новом продукте и нажал на кнопку "Create", этот продукт добавляется в список:

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/new_product2.png "New product")

### Информация о предыдущих днях <a name="day_info"></a>

Если пользователь уже пользовался приложением, у него есть возможность просмотреть информацию за предыдущий день, выбрав интересующий в верхнем правом углу:

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/days.png "Days")

Как только пользователь нажмёт на интересующий день, поля обновятся в соответсвии с имеющейся информацией по этому дню (в том числе и с весом по этому дню).

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/day_info2.png "Day info")

Пользователь может добавить в этот день новый продукт (или изменить вес).

![](https://github.com/gogoJOM/PyFitnessHelper/tree/master/sdoc/source/_static/day_info3.png "Day info")

## Сохренение <a name="save"></a>

У пользователя есть возможность сохранить изменения, нажав на кнопку "Save". Так же сохранение изменений происходит автоматически при закрытии приложения. В том числе и сохранение текущей базы данных продуктов
