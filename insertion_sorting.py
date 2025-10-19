#problem from HackerRank
def insertion_sorting(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j]< arr[j-1] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
arr = [2,4,100,5,1,6,3,0]
insertion_sorting(arr)
print(arr)
            
