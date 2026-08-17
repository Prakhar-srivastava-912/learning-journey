List = [3, 7, 12, 18, 25, 31, 42]
Target = 25
low = 0
high = len(List) - 1
while low <= high:
    mid = (low + high) // 2
    if List[mid] == Target:
        print("Found at index", mid)
        break
    elif Target < List[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Not Found")
