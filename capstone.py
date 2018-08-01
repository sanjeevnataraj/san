def loop(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def recv(n):
    if n==0:
        return 1
    f=1
    if n==1:
        return 1
    return n*recv(n-1)
print("1.using loop\n2.using recursion")
s=int(input())
n=int(input("Enter the number "))
if n>0:
	if s==1:
	    print(loop(n))
	if s==2:
	    print(recv(n))
else:
    print("N should be positive")

