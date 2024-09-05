# https://leetcode.com/problems/maximum-number-of-balloons/description/

text = "loonbalxballpoon"
text ="nlaebolko"
text ="nlaebolko"

main="balloon"

hashMain={}
x=set(main)
for i in x:
    hashMain[i]=main.count(i)
for i in x:
    if i not in text:
        print(0)

hashText={}
t=set(text)
for i in t:
    if i in main:
        hashText[i]=text.count(i)
        hashText[i]=hashText[i]// hashMain[i]
   

res=len(text)
for i in hashText:
    if hashText[i]<res:
        res=hashText[i]
print(res)


