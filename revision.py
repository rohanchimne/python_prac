# ------------ Prime Number ------------------------
# f=0
# for i in range(2,10):
#     f=0
#     for j in range(2,i):
#         if i%2==0:
#             f=1
#             break
#     if f==0:
#         print(i)    


# ---------------- Find count of vowel at particular key in dictionary ----------
# str = 'aeiouAEIOU'
# dic = {1:'fbgaaac', 3:'hdjfdjfa',  2:'ahjdfhsfh'}
# d = {}
# count = 0

# for k,v in dic.items():
#     count=0
#     for j in v:
#         if j in str:
#              count = count+1

#     d[k]=count

# print(d)

# --------------- Fibonacci Series -----------------
# num = int(input("Enter the range: -"))
# x=0
# y=1

# print("{},{}".format(x,y), end=',')

# for i in range(2,num):
#     c=x+y
#     print(c, end=",")
#     x=y
#     y=c

# ----------- Fibonacci way 2 ------------------------
# lst = [0,1]
# for i in range(2,6):
#         c=lst[len(lst)-2] + lst[len(lst)-1]
#         lst.append(c)
#         x=lst[len(lst)-1]
#         y=c
# print(lst)


# -------------- Amstrong Number or not -----------
# num = int(input("Enter a number:- "))
# n=num
# l = len(str(num))
# sum = 0
# for i in range(l):
#     n = num%2
# #     val = n ** l
# #     sum = sum+l
#     print(n)
#     num=int(num/n)
# if n==sum:
#         print(sum) 

# -------------- Amstrong number in a range ------------
# lst=[]
# for n in range(1,200):
#         num=n
#         l = len(str(n))
#         sum = 0
#         for i in range(l):

#                 digit = n%10
#                 val = digit ** l
#                 sum = sum + val

#                 n = int(n/10)

#         if num==sum:
#                 lst.append(num)

# print(lst)


# ---------------- Palindrome program -------------------------
# num = 1
# n = '1232'

# f=0
# for i in range(int(len(n)/2)):
#         if n[i]==n[len(n)-i-1]:
#                 f=0
#         else:
#                 f=1
#                 break
# if f==0:
#         print(num, "Is palindrome")
# else:
#         print(num, "Is not a palindrome")


#-------------- Palindrome logic 2 for numbers -----------------
# n = 121
# l = len(str(n))
# sum=0
# for i in range(l):
#     num=n%10
#     sum=sum+num
#     sum=sum*10
#     n=int(n/10)
# sum=int(sum/10)
# print(sum)


# -------------- Find factorrs of number --------------
# num = 7
# fac=[]
# for i in range(1,num+1):
#     if num%i==0:
#         fac.append(i)
# print(fac)

# ---------------- To remove the empty list using --> pop(index)   -------------
# lst = [[], [1,2,3], [3,4,5], [6,7]]

# for i in range(len(lst)-1):
#     if len(lst[i])==0:
#         lst.pop(i)

# print(lst)

# ---------------- To remove the empty list using --> remove(list)   -------------
# lst = [[], [1,2,3], [3,4,5], [6,7]]

# for i in lst:
#     if len(i)==0:
#         lst.remove(i)

# print(lst)

# ---------------------- to convert list into dictionary  ------------------------
# lst = [[], [1,2,3], [3,4,5], [6,7]]
# d={}
# for i in range(len(lst)):
#     print(lst[i])
#     d[i+1]=lst[i]

# print(d)

# ------------ to convert dictionary into tuple  ------------------
# d = {1:'abc', 2:'bcd', 3:'def'}
# lst = []
# for i in d.items():
#     lst.append(list(i))
# print(lst)

# ----------------- Map keys and values from 2 different list ------------
# lst1 = [1,2,3]
# lst2 = ['abc', 'cdf', 'ghi']
# d={}
# if len(lst1)==len(lst2):
#         for i in range(len(lst1)):
#                 d[lst1[i]]=lst2[i]

# print(d)
    
# ------------------ breaking the list into multiple of 4 -----------
# lst = [1,2,3,4,5,6,7,8]
# s=0
# e=2
# for i in range(4):
#     print("op_{}={}".format(i,lst[s:e]))
#     s=e
#     e=e+2

# --------------------- find the max number in list without using function ----------
# lst = [2,33,6,44,66]
# n = lst[0]
# for i in range(len(lst)-1):
#     if n<lst[i+1]:
#         n=lst[i+1]
#     else:
#         pass
# print(n)


# ------------ sort list without using any function -----------
# lst = [2,1,33,6,44,44,66]

# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if lst[i]<=lst[j]:
#             temp=lst[i]
#             lst[i]=lst[j]
#             lst[j]=temp
# print(lst)

# ----------------- lambda function --------------------
# lst = [2,1,33,6,44,44,66]

# x = list(filter(lambda x: x%2==0, lst))
# x_map = list(map(lambda x: x*2, lst))
# x_red = reduce(lambda x,y: x+y, lst)
# print(x_map)
# print(x_red)
# print(x)

# ---------- Decorators --------------------------

from functools import *
# def decor(func):

#     def inner():
#         x = func() + 11
#         return x
#     return inner    

# @decor
# def fun():
#     return 10

# # x=decor(fun)     --> method 1 with using 
# # res = x()
# # print(res)

# res = fun()
# print(res)

# ------- decorator using the parameter ----------
# def decor(fun):
#     def inner(x,y):
#         res = fun(x,y)+2
#         return res
#     return inner

# @decor
# def fun(a,b):
#     return a+b

# r = fun(10,20)
# print(r)


# ----------- generators ----------
# def gen(x):
#     while x>0:
#         yield x
#         x -=1

# res = gen(10)
# print(list(res))

#------------- count repeated number of items in the list --------------

# lst = [1,1,1,1,2,3,4,4,4,4]
# d={}

# for i in range(len(lst)):
#     count=0
#     for j in range(len(lst)):
#         if lst[i]==lst[j]:
#             count=count+1
#         d[lst[i]]=count 

# for k,v in d.items():
#       if v>1:
#         print(k,'-',v)
# print(d)


#------------------- find prime numbers from the list using function ----------------

# lst = [2,3,4,5,6,7,8,9]

# def pr(lst):
#     f=0
#     for i in lst:
#         f=0
#         for j in range(2,i):
#             if i%j==0:
#                 f=1
#         if f==0:
#             yield i


# res = pr(lst)
# print(list(res))


# --------------- REMOVE DUPLICATE ELEMENTS IN A LIST -------------

# lst = [1,1,12,3,4,4,4,5,6]
#               method 1 using set operator
# lst = list(set(lst))
# print(lst)

#           method 2 using new list
# new_lst = []
# for i in lst:
#     if i in new_lst:
#         pass
#     else:
#         new_lst.append(i)

# print(new_lst)

# -------------- find the particular count of value in a string --------------
# str = 'abcccbdbcccbdboodd'
# find = 'c'
# count=0
# d={}
# for i in str:
#     if find==i:
#         count=count+1

# print('count of {} is {}'.format(find,count))

#-------------------------- but if we want to find the number of charcater counts in a string ----- 
# str = 'abcccbdbcccbdboodd'
# find = 'c'
# count=0
# d={}
# for i in str:
#     count=0
#     for j in str:
#         if i==j:
#             count=count+1

#     d[i]=count
# print(d)

# ------------- hello 



































