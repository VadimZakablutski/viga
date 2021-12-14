from random import *
from module import*
s=pos=neg=loeng=[]
def arvud_loendis():
    """
    :param arv n:int
    :param arv mini:int
    :param arv maxi:int
    :rtype int
    Функция запрашивает кол-во целых чисел которые будут в списке,
    минимальное и максимальное число диапазона, после, с помощью остальных функций показывает списки положиельных,отрицательных,
    средне положительных и средне отрицательных элементов и добавляет в список среднее число.
    """
    print("Данные: ")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini<maxi:
        mini,maxi=vahetus(mini,maxi)
        generator(n,loeng,mini,maxi)
        print()
        print("Результаты:")
        print("Полученный список от",mini,"до",maxi,loeng)
        loeng.sort()
        print("Отсортированный список",loeng)
        jagamine(loeng,pos,neg,noll)
        print("Список положительных элементов",pos)
        print("Список отрицательных элементов",neg)
        print("Список нулевых элементов",noll)
        kesk=keskmine(loeng)
        lisamine(loeng,kesk)
        print("Среднее положительных:",kesk)
        kesk=keskmine(neg)
        lisamine(loeng,kesk)
        print("Среднее отрицательных:",kesk)
        print("Добавляем средние в изначалный массив: ")
        print(loeng)
def vahetus(mini:int,maxi:int):
    """
    Меняет значения переменных местами
    :param arv mini:int
    :param arv maxi:int
    """
    abi=mini
    mini=maxi
    maxi=abi
    return mini,maxi
def generator(n:int,loeng:list,a:int,b:int):
    """
    Генерирует рандомное число в диапазоне а и b и добавляет его/их в список
    """
    for i in range(n):
        loeng.append((randint(a,b)))
def jagamine(loeng:list,p:list,n:list,noll:list):
    """
    Показывает отрицательные и положительные числа и добавляет их в список
    """
    for el in loeng:
        if el>0:
            loeng.append(el)
        else:
            loeng.append(noll)
def keskmine(loeng:list):
    """
    Показывает среднее положительные и средне отрицательные числа
    """
    n=len(loeng)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loeng:
            sum+=i
            kesk=round(sum/n,2)
    return kesk
def lisamine(loeng:list,el):
    """

    :param arv el: int and float
    Программа добавляет среднее отрицательное или среднее положительное в изначальный массив

    """
    loeng.append(el)
    loeng.sort()
arvud_loendis()


