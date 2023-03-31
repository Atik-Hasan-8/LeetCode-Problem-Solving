class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_dict={}
        arr=[[] for _ in range(len(nums)+1)]
        for i in nums:
            my_dict[i]=1+my_dict.get(i,0)
        for n,c in my_dict.items():
            arr[c].append(n)
        res=[]
        for i in range(len(arr)-1,0,-1):
            for n in arr[i]:
                res.append(n)
                if len(res)==k:
                    return res
            
            
        
       
        
        
        
        
        