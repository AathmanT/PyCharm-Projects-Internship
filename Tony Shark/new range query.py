import numpy as np
array = np.array([2,1,1,4,5,1])


n=5
m=6
q=4



print(array)


with open("input.txt","r") as f:
    for line in f:
        a,b=zip(map(int, line.rstrip("\n").split(",")))
        # if(city1<=n and n+1<=city2<=two_n):
        alist = np.where(array == a[0])[0]
        # print(alist[0])
        # print(alist[-1])
        blist = np.where(array == b[0])[0]
        # print("a=",a[0],'b=',b[0])
        # print(alist[0],blist[0])
        # print(-1*array_reverse.index(b[0])-1)
        # print(array.index(a[0]))
        # print(array[array.index(a[0]):-1*array_reverse.index(b[0])-1])
        # print(len(array[array.index(a[0]):-1*array_reverse.index(b[0])-1]))
        if(alist[0]==blist[-1]):
            print("1")
        else:
            print(len(array[alist[0]+1:blist[-1]]))

