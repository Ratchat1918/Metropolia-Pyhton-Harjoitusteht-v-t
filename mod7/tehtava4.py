def list_sum(array):
    array_sum =0
    for i in array:
        array_sum+=i
    return array_sum
array = [1,2,3,4,5,6,7,9,10]
print(list_sum(array))