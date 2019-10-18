n=3
two_n=2*3
m=5

with open("input.txt","r") as f:
    for line in f:
        city1,city2=zip(line.rstrip("\n").split(" "))
        # if(city1<=n and n+1<=city2<=two_n):
        print(city1,city2)


