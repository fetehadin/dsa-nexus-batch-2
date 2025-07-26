class Solution: 
    def selectionSort(self, arr):
        size = len(arr)
        for i in range(size):
            min_idx = i
            for j in range(i+1,size):
                if arr[min_idx]>arr[j]:
                    arr[min_idx],arr[j]=arr[j],arr[min_idx]
        return arr
            
