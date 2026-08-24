def delete_odd(array):
    new_array = array
    for i in new_array:
        if i % 2 !=0:
            new_array.remove(i)
    return new_array
array = [1,2,3,4,5,6,7,8,9,10]
print(delete_odd(array))    