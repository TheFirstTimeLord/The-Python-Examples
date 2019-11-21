if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    a=[]
    [a.append(i) for i in sorted(arr, reverse=True) if i not in a]
    b=0
    for i in a:
        if b==1:
            print i
        b+=1
        