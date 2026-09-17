class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = 0
        for num in nums:
            if num != 0:
                if total == 0:
                    total = 1
                total *= num
            else:
                zero_count += 1
        
        print("has_zero: " + str(zero_count))
        print("total: " + str(total))
        res = []
        for num in nums:
            if zero_count == 1:
                if num != 0:
                    res.append(0)
                else:
                    res.append(int(total))
            elif zero_count > 1:
                res.append(0)
            else:
                res.append(int(total/num))
        return res