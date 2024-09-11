'''
backtracking
permutation of all elements
'''
def permute(arr,l,r):
    if l==r:
        print(arr)
    for i in range(l,r):
        arr[l],arr[i]=arr[i],arr[l]
        permute(arr,l+1,r)
        arr[l],arr[i]=arr[i],arr[l]

# permute([1,2,3,4],0,len([1,2,3,4]))

