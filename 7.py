# переменная для ввода любого числа
n = int(input())

if n % 10 == 1 and n != 11:
    print(str(n) + ' korova')
elif ((n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4)) and n != 12 and n != 13 and n != 14:
    print(str(n) + ' korovy')
else:
    print(str(n) + ' korov')