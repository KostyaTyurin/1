import random

def qsort(list_of_values):
    length = len(list_of_values)
    if length <= 1:
        return list_of_values
    else:
        base_value = random.choice(list_of_values)
        print(base_value)
        min_list = []
        max_list = []
        med_list = []
        for j in list_of_values:
            if j < base_value:
                min_list.append(j)
            elif j > base_value:
                max_list.append(j)
            else:
                med_list.append(j)
        return qsort(min_list) + med_list + qsort(max_list)
    
    
print(qsort([1,2,3,0,10,-1,100]))




