def binarySearch(listData, value):
    low = 0
    high = len(listData) - 1
    while (low <= high):
        mid = (low + high) // 2
        if (listData[mid] == value):
            return mid
        elif (listData[mid] < value):
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr= [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
numerosbuscado = 30
print(f" El numero {numerosbuscado} se encuentra en la posicion {binarySearch(arr,numerosbuscado)}")