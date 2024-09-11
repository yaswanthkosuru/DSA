'''
partition based on pivot element and place all smaller on left and larger on right
'''
def partition_index(arr,i,j):
    pivot=arr[i]
    left=i+1
    right=j-1
    while left<=right:
        while left<=right and arr[left]<pivot:
            left+=1
        while right>=left and arr[right]>pivot:
            right-=1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    arr[i],arr[right] = arr[right],arr[i]
    return right

def quicksort(arr,i,j):
    if i<j:
        pi=partition_index(arr,i,j)
        quicksort(arr,i,pi)
        quicksort(arr,pi+1,j)



arr = [2,-1,-2,-3,4,5,-100,200,-3,-4]

quicksort(arr,0,len(arr))

print('Sorted array is:', arr)