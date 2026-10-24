# 1
# n = int(input())
# if n == 0:
#     print('bishtar az sefr bede')
# else:
#     mylist = []
#     a = 0
#     for i in range(n):
#         x = float(input())
#         mylist.append(x)
#         a = a + x
#     c = a / n
#     for i in range(n):
#         if mylist[i] == c:
#             print(i+1)
#     if c not in mylist:
#         print('hich!')
# -----------
# 2
# n = int(input())
# num = []
# for i in range(n-1):
#     x = int(input())
#     num.append(x)
# for j in range(1,n+1):
#     if j not in num:
#         print(j)
# ---------
# 3
# n = int(input())
# list1 = []
# list2 = []
# for i in range(n):
#     n2 = int(input())
#     list1.append(n2)
# for j in list1:
#     if j not in list2:
#         list2.append(j)
        
# print(list2)
# ----------
# # 4
# a = []
# s = []
# n = int(input())
   
# for i in range(n):
#     x = int(input())
#     a.append(x)
    
# if n == 1 or n == 0:
#     print(a)
# else:

#     s.append(a[-2])
#     s.append(a[-1])

#     for i in range(n-2):
#         s.append(a[i])
#     print(s)

# ---------

# a = []
# y = []
# n = int(input())
# x = int(input())

# for i in range(1,n+1):
#     k = int(input())
#     a.append(k)
    
# for i in range(n-x,n):
#     y.append(a[i])

# for i in range(n-x):
#     y.append(a[i])
    
# print(y)


# ----------
# 1.
# mylist = []
# n = int(input())
# for i in range(n):
#     temp = int(input())
#     mylist.append(temp)

# res = 0
# counter = 0
# for i in mylist:
#     res = res + i
#     counter = counter + 1

# # division by zero
# k = res / counter


# if k in mylist:
#     for j in range(len(mylist)):
#         if mylist[j] == k:
#             print(j + 1)
        
# else:
#     print('hich')

# ----------
# 2.
# n = int(input())
# mylist = []

# for i in range(n-1):
#     a = int(input())
#     mylist.append(a)
    
# for i in range(1,n+1):
#     if i not in mylist:
#         print(i)

# --------
# 3. 
# n = int(input())
# mylist = []
# for i in range(n):
#     a = int(input())
#     if a not in mylist:
#         mylist.append(a)
# print(mylist)
# -------
# 4.
# n = int(input())
# mylist = []
# for i in range(n):
#     a = int(input())
#     mylist.append(a)
# if n > 1:
#     mylist2 = []

#     mylist2.append(mylist[-2])
#     mylist2.append(mylist[-1])
#     del mylist[-1]
#     del mylist[-1]
#     for i in mylist:
#         mylist2.append(i)
        
#     print(mylist2)

# else:
#     print(mylist)

# ------
# rah 2 3
# n = int(input())
# mylist = []
# mylist2 = []
# for i in range(n):
#     a = int(input())
#     mylist.append(a)
    
# c = -2
# for i in range(n):
#     mylist2.append(mylist[c])
#     c = c + 1
# ------
# 5
