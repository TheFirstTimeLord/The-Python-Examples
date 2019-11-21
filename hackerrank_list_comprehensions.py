import math
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    a=max([x,y,z])
    b=a
    c=[]
    d=[]
    e=[]
    g=0
    while b > -1:
        c.append(b) 
        b-=1
    [d.append(i) for i in sorted(c, reverse=True) if i not in d]
    j=len(d)
    k=list('')
    while g < j:
        h=0
        while h < j:
            i=0
            while i < j:
                e=[g,h,i]
                if sum(e)!=n:
                    if h<=y and i<=z and g<=x:
                        k.append(e)
                i+=1
            h+=1
        g+=1
    print(k)