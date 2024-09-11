'''
Radix sort:sort based on radix digits
'''
def counting_sort(arr, exp1):
    n=len(arr)
    output=[0]*n
    count=[0]*10
    for i in range(0,n):
        index=(arr[i]//exp1)%10
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=(arr[i]//exp1)%10
        output[count[index]-1]=arr[i]
        count[index]-=1
        i-=1
    for i in range(0,n):
        arr[i]=output[i]

def radixsort(arr):
    max1=max(arr)
    exp=1
    while max1/exp>0:
        counting_sort(arr,exp)
        exp*=10
    return arr

arr=[170, 45, 75, 90, 802, 24, 2, 66]
print("Sorted array is:", radixsort(arr))