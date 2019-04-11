if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True);
    first = arr[0]
    for i in range(n):
        if arr[i] != first:
            print(arr[i])
            break
