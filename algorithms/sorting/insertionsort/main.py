'''
intution:where to keep element in sorted array if new element comes.
'''
a=[1,2,5,4,3,-1]
def insertion_sort(a):
    n=len(a)
    for j in range(n-2,-1,-1):
        while j+1<n and a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            j+=1
    return a

print(insertion_sort(a))