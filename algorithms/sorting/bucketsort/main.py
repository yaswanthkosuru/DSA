'''
intution:find the current element index in the output array
'''

a=[2,5,10,3,2,10]
def bucketsort(a):
    n=len(a)
    ans=[0]*n
    max_ele=max(a)
    min_ele=min(a)
    bucket=[0]*(max_ele-min_ele+1)
    print(len(bucket))
    for n in a:
        bucket[n-min_ele]+=1
    #accumalate 
    for i in range(1,len(bucket)):
        bucket[i]+=bucket[i-1]
    for i in range(len(a)-1,-1,-1):
        index=bucket[a[i]-min_ele]-1
        ans[index]=a[i]
        bucket[a[i]-min_ele]-=1
    return ans

a=[2,1,2,32,3,2,3,100,20,30,40,10,20]
print(bucketsort(a))
