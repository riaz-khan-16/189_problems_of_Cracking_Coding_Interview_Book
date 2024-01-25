nums=[1,2,3,5,1]


def minimumArrayLength( nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
       
        if len(nums)==1:
            return 1
        def all_element_is_zero(nums):
            for x in nums:
                if x!=0:
                    return False
            return True  
        
        
        while not all_element_is_zero(nums) and len(nums)!=1:
            
                #find  i
                i=0
                while nums[i]==0:
                        i=i+1
                        
                if nums[i+1]:        
                    j=i+1
                    #find  j
                    while nums[j]==0:
                            j=j+1
                print(nums[i],nums[j])
                m=nums[j]%nums[i]

                nums.pop(i)
                nums.pop(j-1)
                nums.append(m)
        
        return len(nums)


print(minimumArrayLength( nums))