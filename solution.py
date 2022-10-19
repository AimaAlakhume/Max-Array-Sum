def maxSubsetSum(arr):
    store = []
    store.append(arr[0])
    store.append(max(arr[0], arr[1]))
    currMax = max(store)
    for i in arr[2:]:
        store.append(max(max(store[-2] + i, i), currMax))
        currMax = max(currMax, store[-1])
    return currMax
