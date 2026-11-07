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
# 6
# n=int(input())
# afrad=[]
# i=1
# while i<=n:
#     afrad.append(i)
#     i=i+1
# marg=1 # vaghti yek bashe yani az aval mikhaim bokoshim va vaghti -1 bashe yani dar in dor nafar aval nemimire
        # dar marhale aval bayad az aval shoroo konim koshtan 
# while len(afrad)>1:
#     print(afrad)
#     zendeha=[] # afradi ke dar in dor zende mimoonan
#     k=marg # baraye koshtan yeki dar mioon age
#     j=0 # andis fardi ke mikahim barresi konim
#     while j<len(afrad):
#         if k<0:
#             zendeha.append(afrad[j])
#         k=k*(-1) # age k == 1 bood dar marhale bad bayad beshe manfi yek ke nakoshim
#         j=j+1
#     if len(afrad)%2==1:
#         marg=marg*(-1)
#     afrad=zendeha
# print(afrad)
# print([])

# -------------
# soal 7
# baraye zir araye motevali ye i daram ke shoroo zir araye ro moshakhas mikone va yek j daram ke payan zir
# araye ro moshakhas mikone. pas i az 0 shoroo mishe ta n , j az i shoroo mishe ta n chon hamishe payan baad
# shoroo ast.
# n = int(input())
# mylist = []
# for i in range(n):
#     mylist.append(int(input()))

# if n > 0 :    
#     max_maj = mylist[0] # bishtarin max ke paida kardim
#     i_max = 0 # i bishtarin baraye khorooji dadan
#     j_max = 0 # j bishtarin baraye khorooje dadan
#     for i in range(len(mylist)):
#         for j in range(i,len(mylist)):
#             maj = 0
#             for k in range(i,j+1):
#                 maj = mylist[k] + maj 
#             if max_maj < maj:
#                 max_maj = maj
#                 i_max = i
#                 j_max = j
                
#     output_list = []
#     print(i_max,j_max)      
#     for k in range(i_max,j_max + 1):
#         output_list.append(mylist[k])
#     print(output_list)
# else:
#     print([])


# -------------
