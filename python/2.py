# 1
# a = []
# for i in range(3):
#     n = int(input())
#     a.append(n)
# print(a)

# -----------
# 2
# nomre = [18,16,10,11,20,14]
# a = 0
# for i in range(0,6):
#     a = a + nomre[i]
# a = a / 6
# if a > 12:
#     print("ghabool shodid")
# -----------
# 3
# n = int(input())
# names = []
# tedad = 0
# for i in range(n):
#     a = input()
#     names.append(a)

# for i in names:
#     if i == 'ali':
#         tedad = tedad + 1
        
# print(tedad)

# -----------
# 4
# a = [1,2,3,4,5,6,7,8,9,10]
# b = []
# for i in a:
#     if i % 2 == 1:
#        b.append(i)
       
# print(b)
# -------------
# 5
# import random
# a = []
# for i in range(10):
#     a.append(input())
    
# # alef
# temp = random.randint(0,9)
# print(a[temp])

# # be
# for i in range(5):
#     print(a[random.randint(0,9)])

# for i in range(5):
#     x = random.randint(0,9-i)
#     print(a[x])
#     del a[x]
# -----------
# 6
# n = int(input())
# m = 0
# mi = 0
# b = []
# for i in range(1, n+1):
#     a = int(input())
#     b.append(a)
#     m = m + a
    
# if n == 0:
#     print('error')
# else:
#     mi = m / n   

# for i in b:
#     if i > mi:
#         print(i)

# ----------------
# 7
# elif khoonde shode ya na?!
# n = int(input())
# if n == 0:
#     print([])
# else:
#     if n == 1:
#         print([1])
#     else:
#         fib = [1 , 1]
#         a = 1
#         b = 1
#         c = 1
#         for i in range(3,n+1):
#             a = b
#             b = c
#             c = a + b
#             fib.append(c)
#         print(fib)

# -------
# 1 
# l = []
# for i in range(1,11):
#     n = int(input())
#     l.append(n)
# print(l)
# --------
# 2
# nomre = [18,16,10,11,20,14]
# a = 0
# t = 0
# for i in nomre:
#     a = a + i
#     t = t + 1
# if a / t > 12:
#     print('ghabool shodid')
# -----------
# # 3.
# n = int(input())
# names = []
# t = 0
# for i in range(n):
#     name = input()
#     names.append(name)
    
# for i in names:
#     if i == 'ali':
#         t = t + 1

# print(t)
# --------
# 4
# adad = [1,2,3,4,5,6,7,8,9,10]
# adad_fard = []
# for i in range(0,10):
#     if adad[i] % 2 != 0:
#         adad_fard.append(adad[i])
# print(adad_fard)
# -----------
# 5
# import random
# a = []
# m = 9
# for i in range(10):
#     n = input()
#     a.append(n)

# # alef
# t = random.randint(0,9)
# print(a[t])

# # b
# for i in range(5):
#     t = random.randint(0,9)
#     print(a[t])
    
# # j
# for i in range(5):
#     t = random.randint(0,m)
#     print(a[t])
#     del a[t]
#     m = m - 1

# ---------------
# 6
# n = int(input())
# l = []
# m = 0
# t = 0

# for i in range(n):
#     x = float(input())
#     l.append(x)
    
# for j in l:
#     m = m + j
#     t = t + 1
# if n == 0:
#     print('error')
# else:
#     k = m / t

# for i in l:
#     if i > k :
#         print(i)
# -------
# 7
# t = 0
# f = [0,1]
# n = int(input())
# if n >= 2:
#     for i in range(n-2):
#             a = f[t]
#             b = f[t + 1]
#             t = t + 1
#             f.append(a+b)
#     print(f)
# else:
#     if n == 1:
#         print([0])
    
    

    