def count_sorting(arr):
    n = len(arr)
    max_elem = max(arr)
    count = [0]*(max_elem + 1)

    for num in arr:
        count[num] += 1
    target = 0   
    for index,value in enumerate(count):
        for j in range(value):
            arr[target]=index
            target += 1
    return arr
#arr = [2,4,1,5,3,2,7,8,9]
#print(count_sorting(arr))
