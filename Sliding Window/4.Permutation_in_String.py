#https://leetcode.com/problems/permutation-in-string/description/

from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    # Length of strings
    len_s1, len_s2 = len(s1), len(s2)
    
    # If s1 is longer than s2, it's impossible for s2 to contain s1's permutation
    if len_s1 > len_s2:
        return False
    
    # Frequency count of characters in s1
    s1_count = Counter(s1)
    # Frequency count of the first window in s2
    window_count = Counter(s2[:len_s1])
    
    # Sliding window over s2
    for i in range(len_s2 - len_s1):
        # If the two frequency counts match, we found a valid permutation
        if s1_count == window_count:
            return True
        
        # Move the window forward: remove the count of the outgoing character
        window_count[s2[i]] -= 1
        if window_count[s2[i]] == 0:
            del window_count[s2[i]]  # Remove the char from counter if its count is zero
            
        # Add the new incoming character to the window
        window_count[s2[i + len_s1]] += 1
    
    # Check the last window
    return s1_count == window_count

# Example Usage:
s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))  # Output: True



