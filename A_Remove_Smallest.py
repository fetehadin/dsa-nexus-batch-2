def solve():
    t = int(input())
    for j in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        for i in range(n-1):
            if arr[i+1] - arr[i] > 1:
                print("NO")
                break
        else:
            print("YES")
if __name__ == "__main__":
    solve()
