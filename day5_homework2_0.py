l1 = [100, 1000, 10, 400, 25, 40, 0]

# 正确方式：拷贝，而不是引用
l2 = l1.copy()  

# 对 l2 从小到大排序
l2.sort()

# 并排打印
print("l1\t l2")
for i in range(len(l1)):
    print(l1[i], "\t", l2[i])