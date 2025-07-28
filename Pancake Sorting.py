class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while end > start:
                arr[start],arr[end]=arr[end],arr[start]
                end -= 1
                start += 1
        output = []
        N = len(arr)
        for i in range(N-1,-1,-1):
            max_idx = i
            for j in range(i,-1,-1):
                if arr[j]>arr[max_idx]: 
                    max_idx=j
            if max_idx!=i:
                flip(max_idx)
                flip(i)
                output.append(max_idx+1)
                output.append(i+1)                  
        return output
