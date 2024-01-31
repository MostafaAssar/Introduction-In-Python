#Enter my list
li = []
print("Enter integers between 1 and 100: ")
for i in range(9):
    li.append(eval(input()))

#using quicksort to sort my list
def partition(array, low, high):
    pivot = array[high]

    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1

def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
 
        quickSort(array, pi + 1, high)

quickSort(li, 0, len(li)-1)

#list without repetation
norep = []
for i in range(len(li)):
    if(li[i] not in norep):
        norep.append(li[i])

#Count occurrence of numbers and print
count = 0
for i in range(len(norep)):
    for j in range(len(li)):
        if (norep[i] == li[j]):
            count += 1

    if (count > 1):
        print(norep[i], " occurs ", count, " times")
    else :
        print(norep[i], " occurs ", count, " time")
    count = 0
