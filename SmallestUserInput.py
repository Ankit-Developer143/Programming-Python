list1 = []
num = int(input("Enter Your Array Length"))

for i in range(1, num+1):
    ele = int(input("Enter Element"))

    list1.append(ele)
    list1.sort()
    print(list1[0])
print(list1)
