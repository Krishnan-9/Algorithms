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
