'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Your code here

#     # return [x for x in arr if x !=0] + [y for y in arr if y ==0]
    
#     lst = []

#     for x in arr:
#         if x !=0:
#             lst.append(x)
#     for y in arr:
#         if y == 0:
#             lst.append(y)
#     return(lst)


def moving_zeroes(arr):
    # initialize a left and right pointer
    # left is 0
    left = 0
    # right is last index in arr
    right = len(arr) - 1
    # while left <= right:
    while left <= right:
        # if left points at a zero and right points at non-zero
        if left ==0 and right != 0:
            # swap left and right items in original arr
            arr[left], arr[right] = arr[right], arr[left]
            # increment left
            left += 1
            right -= 1
            # decrement right
        else:        
            # if left is non-zero:
            if arr[left] != 0:
                left += 1
                # increment left
            # if right is zero:
            if arr[right] == 0:
                # decrement right
                right -= 1

    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")