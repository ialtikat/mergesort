def mergesort(self):
    if len(self)>1:
        mid = len(self)//2
        left = self[:mid]
        right = self[mid:]
        mergesort(left)
        mergesort(right)
        i= j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                self[k]=left[i]
                i=i+1
            else:
                self[k]=right[j]
                j=j+1
            k=k+1
        while i < len(left):
            self[k]=left[i]
            i=i+1
            k=k+1
        while j < len(right):
            self[k]=right[j]
            j=j+1
            k=k+1
    return self
array = [55, 45, 10, 15, 1, 60, 32, 4]
print(mergesort(array))
# Output
# [1, 4, 10, 15, 32, 45, 55, 60]



