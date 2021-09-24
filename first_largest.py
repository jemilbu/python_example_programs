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

def largest_el2(a, loc=False):
    for (i,e) in enumerate(a):
        if e > maxval:
            maxval = e
            maxLoc = i

    if loc == True:
        return maxval, maxLoc
    return maxval

def largest(a,findLoc=False):
    """ Return the largest element of a sequence a. Error Checks
    """
    try: 
        maxVal = a[0]
        maxLoc = 0
        for i in range(1,len(a)):
            if a[i] > maxVal:
                maxVal = a[i]
                maxLoc = i

        if findLoc == True:
            return maxVal, maxLoc
        return maxVal
    except TypeError:
        print("Can't Find Max or Location, Error in Types")
        return -1,-1
    except:
        raise

if __name__ == "__main__":

    a = [1,3,2]
    #r, l = largest(a,True)
    print("Largest element is {:}, Location {:}".format(*largest(a,True)))
