def merge(left,right):
    i,j=0,0
    merged=[]
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
    
    
def mergesort(arr,l,r):
    if l==r:
        return [arr[l]]
    mid=(l+r)//2
    left=mergesort(arr,l,mid)
    right=mergesort(arr,mid+1,r)
    return merge(left,right) #for all intermediate calls it return here

arr=[64, 34, 25, 12, 22, 11, 90]
print("Sorted array is:", mergesort(arr,0,len(arr)-1))