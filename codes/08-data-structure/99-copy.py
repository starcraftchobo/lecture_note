# 할당
a = [1, 2, 3, 4]
b = a
b[0] = 100
print(b)
print(a)# a는 안바뀐다!!!!!!!!!!가아니넹...

#int is immutable
a = 20
b = a
b = 10
print(a)
print(b)

# 얕은 복사
a = [1, 2, 3]
b = a[:]
c = a.copy()

b[0] = 100
c[0] = 999
print(a)
print(b)
print(c)

# 얕은 복사의 한계
a = [1, 2, [3, 4, 5]]
b= a[:]

b[0] = 999
b[2][1] = 1234
print(a)
print(b)

# 깊은 복사
import copy
a = [1, 2, [3, 4, 5]]
b= copy.deepcopy(a)

b[2][1] = 1234
print(a)
print(b)