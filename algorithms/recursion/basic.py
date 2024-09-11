'''
normal recursion
base case return 1
function calls another function and waits for the result.
'''
def fact(n):
    if n:
        return n * fact(n-1)
    return 1
print(fact(10))

'''
function calls two another function and waits for the result
fibanoci
TC:2^n
'''
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(3))

'''
function calls k another function and waits for the result
k-bonacci sequence
TC:k^n
'''
def kbonacci(n,k):
    if n<k:
        return n
    ans=0
    for i in range(1,k+1):
        ans+=kbonacci(n-i,k)
    return ans
print(kbonacci(10,2))
