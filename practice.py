def array123(nums):
    "Given an array of ints,return True if .. 1, 2, 3, .. appears in the array somewhere.  "

    if nums is None or len(nums) == 0:
        return False
    hlst = {1: 1, 2: 2, 3: 3}

    for n in nums:

        if n in hlst:
            del hlst[n]
        if len(hlst) == 0:  # We've found them all!
            return True
    return False

ret = array123([0,2,3,1])

print (ret)



