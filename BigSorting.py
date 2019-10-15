#https://www.hackerrank.com/challenges/big-sorting/problem

def bigSorting(unsorted):
    # sorting done using x as well as len(x)
    unsorted.sort(key= lambda x:(len(x),x))
    return unsorted