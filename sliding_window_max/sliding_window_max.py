'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # Your code here
    n = len(nums) # length of array
    start = 0 # starting point
    stored = [] # list which will store max values
    while k <= n:
        window = nums[start:k] # assign window and move it by one through eterations
        start += 1
        k += 1
        stored.append(max(window))
    return stored

         
# print(max(nums[:k]))


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
