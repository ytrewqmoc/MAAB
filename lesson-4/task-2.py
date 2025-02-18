def uncommon_elements(list1, list2):
    from collections import Counter
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = []
    for num in count1:
        if num not in count2:
            result.extend([num] * count1[num])
    for num in count2:
        if num not in count1:
            result.extend([num] * count2[num])
            return result
print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6]))
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))
