a = [4, 6, 3, 2, 7, 5, 4, 6, 8, 9, 4, 1, 2, 5, 5]
n = len(a)
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
for i in range(n-1, 0, -1):
    if a[i] == a[i-1]:
        print(a[i])
        break
else:
    print("Not any")
  
