
# Given an array of integers A and let n to be its length.
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
# Calculate the maximum value of F(0), F(1), ..., F(n-1).

# Note:
# n is guaranteed to be less than 10^5.

# For every rotation, we add the sum of all elements in the array
# and subtract the length * the k - 1 element to calculate the 
# rotation, then measure the current rotation's sum against 
# the current maximum of all rotations to return a final max

def maxRotateFunction(A):
    """
    :type A: List[int]
    :rtype: int
    """
    length = len(A)
    curr = 0
    acc = 0
    
    # calculates the initial rotation and logs the
    # sum of all the elements
    for i in range(length):
        curr += i * A[i]
        acc += A[i]
        
    curr_max = curr

    for i in range(length - 1, 0, - 1):
        # context: test = [4,3,2,6]
        # for each iteration, add the sum of all elements in the array and subtract
        # the contributions from n - 1 since f(1) = 1*a[0] + 2*a[1] + 3*a[2] + 0*a[3]
        # reduced -> 1*4 + 2*3 + 3*2 + 0
        curr = curr + acc - length*A[i]
        curr_max = max(curr, curr_max)
        
    return curr_max