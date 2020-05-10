# Проект Fitness Helper

Выполненный проект представляет собой приложение, позволяющее пользователю вести подсчёт употребляемого количества килокаллорий в день и запись текущего веса.

## Выбор пользователя

При запуске приложения пользователю предлагается выбрать аккаунт, существует 2 возможности:

### Создание нового пользователя.

Для этого нужно заполнить все поля таблицы в левом верхнем углу окна и нажать кнопку "Create new user".

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/new_user_info.png "Create new user")

Если пользователь с таким именем существует, приложение выдаст информацию об ошибке:

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/warning_username.png "Error message")

Так же ошибка может возникнуть, если какое-либо поле при создании пользователя не было заполнено:

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/warning_weight.png "Error message")

### Выбор уже существуещего пользователя.

Если пользователь уже пользовался приложением, он может выбрать свой аккаунт и нажать кнопку "Choose user".

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/choose_user.png "Choose user")

Если пользователь не был выбран (остался "New"), а кнопка нажата, пользователь опять получит информацию об ошибке.

## Таблица с информацией

Сразу после выбора/создания пользователя, загружаются поля с информацией по текущему дню и функционалом по добавлению новой информации.
По умолчанию день выбран как текущий.

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/day_info1.png "Day info")

### Добавление продукта в текущий день

Для того, чтобы добавить новый продукт, под таблицей пользователь может выбрать время приёма пищи:

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/add_product1.png "Add product")

Затем выбрать продукт из уже существующих в базе данных:

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/add_product2.png "Add product")

Ввести употреблённое количество и нажать кнопку "Add":

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/add_product3.png "Add product")

После чего таблица с информацией автоматически обновится:

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/add_product4.png "Add product")

### Создание нового продукта

### Информация о предыдущих днях

Если пользователь уже пользовался приложением, у него есть возможность просмотреть информацию за предыдущий день, выбрав интересующий в верхнем правом углу:

![alt-текст](https://github.com/gogoJOM/PyFitnessHelper/blob/master/img/days.png "Days")

