*********************
Установка
*********************

Сборка пакета
=====================

Чтобы собрать package на python достаточно воспользоваться командой (понадобятся setuptools и wheel)::

   python setup.py bdist_wheel

Далее можно через pip ставить созданный whl файл.

Для запуска проекта (если он установлен как package) нужны комманды::

   import PyFitnessPackage.run_app
   PyFitnessPackage.run_app.run_helper()
   
Запуск исходного файла
======================

Либо можно скопировать репозиторий::

   git clone https://github.com/gogoJOM/PyFitnessHelper

Если запуск происходит под Windows, нужно установить необходимые пакеты::

   pip install -r requirements.txt

Затем, чтобы запустить приложение, достаточно следующей команды::

   python main.py
   
Тесты
=====

Тесты запускаются с помощью модуля pytest, файл - ```PyFitnessPackage/tests.py```. Для запуска достаточно запустить команду::

   pytest PyFitnessPackage/tests.py
   