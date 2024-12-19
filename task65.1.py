arr = [7, 3, 13, 9, 7, 8, 2, 13, 11]

arr.sort(reverse=True)

num = int(input("Введите число для поиска: "))

result = [x for x in arr if x == num]

if len(result) > 0:
    print("Число", num, "найдено в отсортированном массиве")
    print("Индексы числа", num, "в отсортированном массиве:")
    for i, x in enumerate(arr):
        if x == num:
            print(i)
else:
    print("Число", num, "не найдено в отсортированном массиве")
  
