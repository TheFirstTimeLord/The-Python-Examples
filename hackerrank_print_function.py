from __future__ import print_function
import math
if __name__ == '__main__':
    n=int(raw_input())
    #print(n[1],n[2],n[3])
    y=0
    for i in range(1, n+1):
        x=int(math.log10(i))+1  
        y=y*(10**x)+i
    print(y)