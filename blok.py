first = input("Введите число: ")
second = input("Введите число: ")
third = input("Введите число: ")
if first == second == third:
    print(3)
elif second == first:
    print(2)
elif first == third:
    print(2)
elif second == third:
    print(2)
else:
    print(0)
