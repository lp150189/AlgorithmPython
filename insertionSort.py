def print_huy():
    print "huy"

def insertionSort(array):
    for i in range (0, len(array)):
        print array[i]

def printBackward(array):
    for i in range (len(array)-1,0-1,-1):
        print array[i]

array =[1,2,3,4,5]
print_huy()
#printBackward([1,2,3,4,5])
insertionSort(array)
