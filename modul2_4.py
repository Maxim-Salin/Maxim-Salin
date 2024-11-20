numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
i=0
j=0
value = 0
mrPrim = False
for i in range(len(numbers)): # цикл перебора списка
    j = int(numbers[i])
    mrPrim = False   # бнуление маркера в основном цикле перебора
    for j in range(2, int(numbers[i])): # вложенный цикл перебора простых чисел
        if int(numbers[i]) % j == 0:
            mrPrim = True  # маркер составного числа
    if mrPrim == True:
           primes.append(numbers[i])
    else:
        if numbers[i] != 1:  # 1 - испключение
            not_primes.append(numbers[i])

print(primes)
print(not_primes)