def combinedarray(nums1,nums2):
    i = 0
    j = 0
    sortedlist = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            sortedlist.append(nums1[i])
            i += 1
        else:
            sortedlist.append(nums2[j])
            j += 1
    for x in range(i,len(nums1)):
        sortedlist.append(nums1[x])
    for c in range(i, len(nums2)):
        sortedlist.append(nums2[c])
    return sortedlist
nums1 = [1,2,3,4,9]
nums2 = [2,5,6]
print(combinedarray(nums1,nums2))
