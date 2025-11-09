arr1 = [4,7,8,9,11,65]
arr2 = [2,6,9,34,56,78,79]
def merge_arr(arr1,arr2):
    size_1 = len(arr1)
    size_2 = len(arr2)
    p_1 = 0
    p_2 = 0
    result = []
    while p_1 < size_1 and p_2 < size_2:
        if arr1[p_1]<arr2[p_2]:
            result.append(arr1[p_1])
            p_1 += 1
        else:
            result.append(arr2[p_2])
            p_2 += 1
    result.extend(arr1[p_1:])
    result.extend(arr2[p_2:])
    return result
print(merge_arr(arr1,arr2))
