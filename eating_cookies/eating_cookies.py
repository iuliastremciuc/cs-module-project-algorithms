'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
#     # Your code here
    
#     if n == 0: # base: there are no more cookies
#         return 1
#     elif n < 0: # check for negetive values
#         return 0

#     # this represents our recursive case
#     # three possible decisions
#     # eat 1 cookie, 2 coockies or 3 cookies

#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n - 3)



def eating_cookies(n, cache = None): # "cache" can be any name variable  
    print(n)
    #base case
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the work has alredy been done
    # by looking in the cache
    elif cache is not None and cache[n] > 0:
        return cache[n]

    else:
        # might need to create our cache for the first time
        if cache is None:
            # initialize an empty list for cache
            cache = [0 for i in range(n+1)]

        # store the value of  the recursive call expressions in our cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n - 3, cache)
    return cache[n]


    # pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
