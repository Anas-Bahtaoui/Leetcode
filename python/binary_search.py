
def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]
    x = 5

    result = binary_search(arr, x)

    if result != -1:
        print("Element is present at index %d" % result)
    else:
        print("Element is not present in array")