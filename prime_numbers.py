# prime number definition:
# n % 1 == 0 and # m % m == 0 <-- definition of integer
# only % 1 and % m are zero. any number smaller than the number, if modulo'd, will be > 0.
# a good function will run all integers until n > 100, or while n <= 100
# for item in range[:n]:
# if n % item == 0 and (item !=1 or item !=n), then continue. else: empty_list.append(n)

# list_b=[]
# for n in range(100):
#     for i in range(n):
#         if i == 0:
#             continue
#         if i != 1 and i != n and n % i == 0:
#             break
#         else:
#             list_b.append(i)

# print(list_b)

# I want a number for which no integer in range(number) other than 1 and number modulo to zero.

list_b = []
for n in range(100):
    if n > 1:
        for i in range(2,n):
            if i > 1:
                if (n % i) == 0:
                    break
        else: 
            if n not in list_b:
                list_b.append(n)

print(list_b)