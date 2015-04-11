import makeBigList
def merge_sort( thelist):
    #the base case when the size of thelist =1
    if len(thelist)==1:
        return thelist
    first_half = merge_sort(thelist[0:len(thelist)/2])
    second_half = merge_sort(thelist[len(thelist)/2:len(thelist)])
    return merge_2_list(first_half,second_half)

def merge_2_list(first_half, second_half):
    #make the list of size= first_half+second_half
    thelist=[]
    list_pointer=0
    pointer1=0
    pointer2=0
    while pointer1<len(first_half) and pointer2<len(second_half):
        print pointer1
        print pointer2
        print list_pointer
        if first_half[pointer1]<second_half[pointer2]:
            thelist.append(first_half[pointer1])
            pointer1+=1
            list_pointer+=1
        else:
            thelist.append(second_half[pointer2])
            pointer2+=1
            list_pointer+=1
    if pointer1 == len(first_half):
        #copy over the second list to the final list
        for i in range (pointer2, len(second_half)):
            thelist.append(second_half[i])
    elif pointer2 == len(second_half):
        #copy over the first list to the final list
        for i in range (pointer1, len(first_half)):
            thelist.append(first_half[i])

    return thelist

list1 =[2,7,19,25]
list2 = [3,6,8,17,21,22,30,100,120,300]
thelist = merge_2_list(list1,list2)
print str(thelist).strip('[]')

listtest= [5,1,100,2,0,3,9]
half1 = listtest[0:len(listtest)/2]
half2 = listtest[len(listtest)/2:len(listtest)]
print str(half1).strip('[]')
print str(half2).strip('[]')

print str(merge_sort(listtest)).strip('[]')

biglist = makeBigList.makeBigList(200)
print str(merge_sort(biglist)).strip('[]')

