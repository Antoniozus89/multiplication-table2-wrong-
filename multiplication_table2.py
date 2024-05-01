
list1_ = [7, 8, 9, 10]
list2_ = [5, 6]
print('    5   6')
for i in list1_:
    print(i, end='\t')
    for j in list2_:
         print((i*j), end='\t')
    print( )
