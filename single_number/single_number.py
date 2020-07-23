'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
''' 

## my solution
# def single_number(arr):
#     num = 0
#     for i in arr:
#         num ^= i
#     return num    
  

# Matt's first pass solution
    
def single_number(nums):
    no_dups = [] # list will hold numbers we see in the nums array
    for num in nums: # iterate through nums
        # check if the number is already in the 'no_dups' array
        if num not in no_dups:  # O(1)
            no_dups.append(num) # O(1)
        # if it is remove from no_dups array
        else:
            no_dups.remove(num) # O(n)
    return no_dups[0]

# Matt's optimization

def single_number(nums): # O(n)
    counts = {}
    # iterate through nums
    for num in nums: # O(n)
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
​
    for k, v in counts.items(): # O(n)
        if v == 1:
            return k



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")