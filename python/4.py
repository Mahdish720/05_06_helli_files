# n = int(input())
# mylist = []
# miane = 0

# for i in range(n):
#     temp = int(input())
#     mylist.append(temp)

# for i in range(len(mylist)):
#     kamtar = 0
#     bishtar = 0
#     for j in range(len(mylist)):
        # tebgh tozihat daghigh soal ke gofte daghighan che chizi ro bayad miane farz konim shart mosavi , ...
        # bardashte shod. ba in tozihat list [1,2,2,2,5] ham miane nadare. vali age bekhaim ain ghabl dar nazar
        # begirim hamoon sort konim va vasati ro be onvan miane dar nazar begirim rahat tarim :))
#         if mylist[j] < mylist[i] :
#             kamtar = kamtar + 1
            
#         if mylist[j] > mylist[i] :
#             bishtar = bishtar + 1
    
#     if kamtar == bishtar and kamtar == n//2:
#         print(mylist[i])


# ------------
# n = int(input())
# A = []
# for i in range(n) :
#     A.append(int(input()))

# k = int(input())
# B = []
# for i in range(k) :
#     B.append(int(input()))

# i = 0
# j = 0
# C = []


# while (len(C) != (len(A) + len(B))) :
    
#     if len(A) > i :
#         a = A[i]
#     if len(B)>j :
#         b = B[j]
    
#     if len(A) > i and len(B) > j :
#         if a < b :
#             C.append(a)
#             i += 1
#         else :
#             C.append(b)
#             j += 1
    
#     else:
#         if i >= len(A) and j < len(B) :
#             C.append(b)
#             j += 1
        
#         if j >= len(B) and i < len(A) :
#             C.append(a)
#             i += 1
    
# print(C)
# -------------
# 6
# n = int(input())
# mylist = []
# for i in range(2,n):
#     flag = 1
#     for j in mylist:
#         if i % j == 0:
#             flag = 0
#     if flag == 1:
#         mylist.append(i)
# print(mylist)
# --------
# 7
# a = [4,8,7,1,0,-5,-7]
# output = []

# # paida kardan bishtarin ozv yek lise ke khorooji bede.
# def find_max(lst):
#     if len(lst) > 0 :
#         mymax = lst[0]
#         for i in lst:
#             if mymax < i:
#                 mymax = i
#         return mymax
#     else:
#         return "hichi"


# for i in range(len(a)):
    
#     if i % 2 == 0: # dafat zoj bayad be samt chap ezafe she
#         output.insert(0,a.pop(a.index(find_max(a)))) # bishtarn ozv ro paida mikonim. 
#         # andise bishtarin ozv ro paida mikonim. oon ozv ro az a pop mikonim , be samt chap ezafe mikonim
#     else: # dafat fard bayad be samt rast ezafe she
#         output.append(a.pop(a.index(find_max(a))))
        
# print(output)