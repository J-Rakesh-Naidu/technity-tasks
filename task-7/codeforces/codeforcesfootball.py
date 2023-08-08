t = input()
count1 = 0
count0 = 0
y = "NO"
for x in t:
    if x == "1":
        count1 += 1
        count0 = 0
    elif x == "0":
        count0 += 1
        count1 = 0
    if count0 >= 7 or count1 >= 7:
        y = "YES"
        break
print(y)
