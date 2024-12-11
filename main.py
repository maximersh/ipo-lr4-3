n = int(input("vvedi:"))
a = [i for i in range(n+1)]
print (*a)
a[1] = 0
i = 2
while 1 < n ** 0.5: 
    if a[i] != 0:
        j = i ** 2
while j <= n:
    a[j] = 0
    j = j + i
    i = i + 1
    a = [i for i in a if a[i] !=0]
    print (*a)
