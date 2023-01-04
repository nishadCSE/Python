n=int(input())
arr=map(int,input().split())
z=list(set(sorted(arr)))
print(z[-2])