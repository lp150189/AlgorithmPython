import makeBigList
def print_huy():
    print "huy"

def insertionSort(array):
    for i in range (1, len(array)):
        for j in range (i,0-1, -1):
            if array[i]< array[j]:
                swap(array, i, j)
                i = j
    return array

def swap(array, i, j):
    temp =array[i]
    array[i] = array[j]
    array[j] = temp
                

def printBackward(array):
    for i in range (len(array)-1,0-1,-1):
        print array[i]

array =[1,2,3,4,5]

swap(array,0,4)
print str(array).strip('[]')

print "let's sort it"
insertionSort(array)
print str(array).strip('[]')

thelist = makeBigList.makeBigList(10)
print str(thelist).strip('[]')
insertionSort(thelist)
print str(thelist).strip('[]')
