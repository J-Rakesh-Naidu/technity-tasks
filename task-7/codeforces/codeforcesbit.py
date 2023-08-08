t = int(input())
statements = []
for _ in range(t):
    y = input()
    statements.append(y)
x = 0
for i in statements:
    if i[1] == "+":
        x += 1
    elif i[1] == "-":
        x -= 1
print(x)
