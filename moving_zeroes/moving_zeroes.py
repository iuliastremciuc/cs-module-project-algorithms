'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # return [x for x in arr if x !=0] + [y for y in arr if y ==0]
    lst = []

    for x in arr:
        if x !=0:
            lst.append(x)
    for y in arr:
        if y == 0:
            lst.append(y)
    return(lst)


    # pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")