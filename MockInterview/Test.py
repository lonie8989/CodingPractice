# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Hashmap 
# a=3 -> 2
# r=1 -> r=0 -> pop
# < c = 3 ++ 
# if it's not 

# curr = "c"
# if not curr in Hashmap:
#     hashmap[curr] = 1

# Input: String="araaccci", K=2
# Output: 5
# Explanation: The longest substring with no more than '2' distinct characters is "aaccc".

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

def Kdistinct(self, s, k):
    h = {}
    res = 0

    for c in s:
        if 
        if not c in h:
            h[c] = 1
        else:
            h[c] += 1

        # if hashmap size == k+1: current hashmap's value
            while ...
                # inrement or pop character count until hashmap size == K
            
    
    

