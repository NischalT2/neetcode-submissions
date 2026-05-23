class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 0
        containsOneZero = False
        containsMulZero = False
        for num in nums:
            if containsOneZero and num == 0:
                containsMulZero = True
            elif num == 0:
                containsOneZero = True
            if num != 0:
                if product == 0 and num != 0:
                    product += num
                else:
                    product *= num
        
        output = []
        for num in nums:
            if containsMulZero:
                output.append(0)
            else:
                if containsOneZero:
                    if num == 0:
                        output.append(product)
                    else:
                        output.append(0)
                else:
                    output.append(product // num)
        return output