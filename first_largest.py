"""
Python program to find the largest element and its location.
"""

def largest_element(a,findLoc=False):
    """ Return the largest element of a sequence a.
    """
    maxVal = a[0]
    maxLoc = 0
    for i in range(1,len(a)):
        if a[i] > maxVal:
            maxVal = a[i]
            maxLoc = i

    if findLoc == True:
        return maxVal, maxLoc
    return maxVal

if __name__ == "__main__":

    a = [1,2,3,2,1]
    r,l = largest_element(a,True)
    print("Largest element is {:}, Location {:}".format(r,l))
