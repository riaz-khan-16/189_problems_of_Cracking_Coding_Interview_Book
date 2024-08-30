
#https://leetcode.com/problems/valid-parentheses/description/
s = "()[]{}"
s="(])"

stack=[]

hash={')':'(',
      '}':'{',
      ']':'[',
      }

for i in s:
    if not stack:
        stack.append(i)
    elif i in hash:
        if stack[-1]==hash[i]:
            stack.pop()
        else:
            stack.append(i)
    else:
        stack.append(i)
print(stack)
    