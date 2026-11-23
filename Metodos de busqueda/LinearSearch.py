def linearSearch(listData, value):
    index = 0

    while index < len(listData):
        if listData[index] == value:
            return index
        index += 1
    return -1
  
arr= [-12, 11, 12, 22, 25, 34, 64, 64, 90, 90, 90, 90]
numerosbuscado = 12
print(f" El numero {numerosbuscado} se encuentra en la posicion {linearSearch(arr,numerosbuscado)}")