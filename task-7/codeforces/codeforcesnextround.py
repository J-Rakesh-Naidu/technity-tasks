n,k = map(int,input().split())
contestants = list(map(int, input().split()))
count = 0
for i in contestants:
    if i > 0 and i >= contestants[k-1]:
        count += 1
print(count)
