def find_missing(alist):
    ...:     all_negative = True
    ...:     for item in alist:
    ...:         if item >=1:
    ...:             all_negative = False
    ...:             break
    ...:     if all_negative:
    ...:         return 1
    ...:     # there are positive number
    ...:     #traverse the numbers and mark the number as visited with true
    ...:     check_list = [True for i in range(1000000)]
    ...:     for i in alist:
    ...:         if i >= 1:
    ...:             # only then process
    ...:             check_list[i] = False
    ...:     #now go throught the lost
    ...:     print(check_list[:20])
    ...:     for index, item in enumerate(check_list):
    ...:         if item and index !=0:
    ...:             print(index)
    ...:             return
    ...:
    ...:
