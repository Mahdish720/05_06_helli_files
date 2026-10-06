# 1
# n = int(input())
# maj = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         maj = maj + i
        
# print(maj)

# ------------
# 2
# na = 0
# np = 0

# for i in range(1,21):
#     n = float(input())
#     if n > na :
#         na = n
#         np = i
        
# print(np)
# -------------
# 3
# a = 1
# maj = 0
# tedad = 0
# while a == 1:
#     n = int(input())
#     tedad = tedad + 1
#     maj = maj + n
#     if n == 0:
#         a = 0
# if (tedad-1) != 0:
#     print(maj/(tedad-1))
# else:
#     print("error")

# ------------
# 4
# def mooz(n):
#     x=0
#     num=2
    
#     while x<n:
#         adad= 1
        
#         for i in range(2,num):
#             if num % i==0:
#                 adad=0
        
#         if adad==1:
#             x=x+1
        
#         num=num+1
    
#     return num-1

# n=int(input())
# r=mooz(n)
# print(r)

# ---------
# import random

# n = random.randint(1,20)
# print(mooz(n))

# -------------
# def zarb(n):
#     t = 1
#     if n == 0:
#         return  0
    
#     while n != 0:
#         e = n % 10
#         t = t * e
#         n = n // 10
#     return t

# print(zarb(0))

# --------

# def soudi_check(n):
#     last_digit = 10
#     checker = 1
#     while n != 0:
#         digit = n % 10
#         n//=10
#         if digit > last_digit:
#             checker = 0
#         last_digit = digit
#     return checker

# n = int(input())
# for i in range(10**(n-1),10**n):
#     if soudi_check(i) == 1:
#         print(i)

# ----------
# 1.

# n = int(input())
# t = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         t = t + i
# print(t)
# ---------------
# 2.
# t = -1
# m = 0
# for i in range(1,21):
#     n = float(input())
#     if n > t:
#         t = n
#         m = i
# print(m)
# ---------
# 3.
# x = 0 # maj
# y = 0 # tedad
# z = 1 # flag
# while z == 1:
#     n = int(input())
#     if n != 0:
#         x = x + n
#         y = y + 1
#     else:
#         z = z + 1
# if y != 0:
#     print(x/y)
# else:
#     print('error')

# --------
def aval(n):
    i = 0 # tedada adad aval
    m = 0 # check aval
    t = 1 # adad
    while i != n :
        t = t + 1
        for j in range(2,t):
            if t % j == 0:
                m = 1
        if m == 0:
            i = i + 1
        m = 0

    print(t)
    
