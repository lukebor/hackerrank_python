# Enter your code here. Read input from STDIN. Print output to STDOUT



import sys
suma=0
nk = list(map(int, input().rstrip().split()))
n=nk[0]
k=nk[1]
ar = list(map(int, input().rstrip().split()))
b=int(input())
#print(ar)
suma=int(b-(sum(ar)-ar[k])/2)
if not suma:
    print('Bon Appetit')
else: print(suma)