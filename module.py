from random import *
def arvud_loendis():
    print("Данные: ")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    a=int(input("Введите минимальное число диапазона => "))
    b=int(input("Введите максимальное число диапазона => "))
    if a<b:
        vahetus(a,b)
        generator(n,loeng,a,b)
        print()
        print("Результаты:")
        print("Полученный список от",a,"до",b,loeng)
        loeng.sort()
        print("Отсортированный список",loeng)
        jagamine(loeng,p,n,noll)
        print("Список положительных элементов",p)
        print("Список отрицательных элементов",n)
        print("Список нулевых элементов",noll)
        kesk=keskmine(loeng,n)
        lisamine(loend,l,kesk)
        print("Среднее положительных:",kesk)
        kesk=keskmine(loeng,n)
        lisamine(loeng,el,kesk)
        print("Среднее отрицательных:",kesk)
        print("Добавляем средние в изначалный массив:")
        loeng.sort
        print(loeng)
def vahetus(a,b):
    a="abi"
    a=b
    b="abi"
    return a,b
def generator(n,loeng,a,b):
    for i in range(n):
        loend.append((randint(a,b)))
def jagamine(loeng,p,n,noll):
    for el in loeng:
        if el>0:
            loeng.append(el)
        else:
            loeng.append(noll)
def keskmine(loeng,n):
    n=len(loeng)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
            kesk=round(sum/n,2)
    return kesk
def lisamine(loeng,el):
    loeng.append(el)
    loeng.sort()
arvud_loendis()


