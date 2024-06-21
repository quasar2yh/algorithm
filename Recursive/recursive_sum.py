"""
li = [1,2,[1,2,3,4],5,8,10,[1,2,3,8,9],.....] 합산
"""

li = [1,2,[1,2,3,4],5,8,10,[1,2,3,8,9]]

total = 0

def sum_function(obj):
    global total
    if isinstance(obj, int):
        total += obj
    else:
        for i in obj:
            sum_function(i)
    return total

print(sum_function(li))


