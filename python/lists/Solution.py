if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        method = input().split()
        if method[0] == 'insert' :
            list.insert(int(method[1]), int(method[2]))
        elif method[0] == 'remove' :
            list.remove(int(method[1]))
        elif method[0] == 'append' :
            list.append(int(method[1]))
        elif method[0] == 'sort' :
            list.sort()
        elif method[0] == 'pop' :
            list.pop()
        elif method[0] == 'reverse' :
            list.reverse()
        elif method[0] == 'print' :
            print(list)