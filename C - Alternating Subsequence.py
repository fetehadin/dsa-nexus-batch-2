def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        total_sum = 0
        i = 0
        while i < n:
            j = i
            current_max = arr[i]
            # Move j until sign changes
            while j < n and (arr[j] * arr[i] > 0):
                current_max = max(current_max, arr[j])
                j += 1
            total_sum += current_max  
            i = j
        print(total_sum)
if __name__ == "__main__":
    solve()
