#5. Longest Palindromic Substring

#brute force approach

s = "babad"


def brute_Force(s):
    for k in range(len(s)-1,-1,-1):
        for i in range(0,len(s)-k):
            x=s[i:i+1+k]

            if x==x[::-1]:
                return x
            
#DP Approach            
def dynamic_programming(s):
    if len(s) <= 1:
        return s
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    max_str = s[0]

    for i in range(len(s) - 1):
        odd = expand_from_center(i, i)
        even = expand_from_center(i, i + 1)

        if len(odd) > len(max_str):
            max_str = odd
        if len(even) > len(max_str):
            max_str = even

    return max_str


