word1 = "horse"
word2 = "ros"
def helper(i: int, j: int) -> int:
        if i == 0:
            return j
        if j == 0:
            return i
        
      
        if word1[i - 1] == word2[j - 1]:
            return helper(i - 1, j - 1)
        else:
          
            insert_op = helper(i, j - 1)    # Inserting in word1
            delete_op = helper(i - 1, j)    # Deleting from word1
            replace_op = helper(i - 1, j - 1)  # Replacing in word1
            
         
            return 1 + min(insert_op, delete_op, replace_op)

    
res=helper(len(word1), len(word2))
print(res)




