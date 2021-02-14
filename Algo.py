# TYPES OF SORTING ALGORITHMS

# 1. Insertion sort
def create_array(*array, random=False):
    # create interface
    string = array[0]
    ls = string.split()
    ls = list(map(int, ls))
    print(ls)
    # algo
    n=len(ls)
    for i in range(1,n):
        j = i-1
        var = ls[i]
        while j>=0 and ls[j]>var:
            ls[j+1] = ls[j]
            ls[j] = var
            j-=1
        else:
            pass

        print(ls)


inp = input("enter")
create_array(inp)

# 2. Selection sort
def get_min_index(ls):
    min = ls[0]
    for j in range(1, len(ls)):
        if j < len(ls) and ls[j] < min:
            min = ls[j]
            print(min)
    return ls.index(min)



def selection_sort(ls):
    j=0
    while j<len(ls):
        min_index = get_min_index(ls[j:]) + j
        if ls[j]>ls[min_index]:
            ls[j], ls[min_index] = ls[min_index], ls[j]
            j+=1
        else:
            j+=1

    return ls
A = [8,4,6,6,7,2,2,34,5,6,7,8,8]
print(selection_sort(A))
