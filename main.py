vvod_ot_polzovatelya = int(input("введите число:"))
spisok = [i for i in range(2, vvod_ot_polzovatelya + 1)]
p = 0
while p <= len(spisok) - 1:
    i = spisok[p]
    for item in spisok:
        if (item % i == 0) and (item > i):
             spisok.remove(item)
    if vvod_ot_polzovatelya not in spisok:
        print(f"число {vvod_ot_polzovatelya} не является простым")
        break
    p +=1
if vvod_ot_polzovatelya in spisok:
    print(f"число {vvod_ot_polzovatelya} является простым")

