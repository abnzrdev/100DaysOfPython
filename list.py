size = input("")
lst = []
for i in range(int(size)):
    num = int(input(""))
    lst.append(num)

for i in range(len(lst)):
    if lst[i - 1] < lst[i] and i != 0:
        print(lst[i - 1])
    else:
        print(-1)