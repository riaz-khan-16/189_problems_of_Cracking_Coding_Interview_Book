# https://leetcode.com/problems/unique-email-addresses/


def process_local(local):
    new=''
    for i in local:
        if i!='.':
            new=new+i
        if i=='+':
            return new[:-1]
    return new


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
unique=set()
for i in emails:
    #seperate domain and local
    x=i.split('@')
    local=x[0]
    domain=x[1]
    local=process_local(local)
    unique.add(local+'@'+domain)
print(len(unique))


