#https://leetcode.com/problems/isomorphic-strings/description/


s = "egg"
t = "add"
def make_hashmap(word):
    s=set(word)
    hash={}
    for i in s:
        hash[i]=word.count(i)
    return hash
print(make_hashmap(s))
print(make_hashmap(t))